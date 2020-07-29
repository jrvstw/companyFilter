import sys
import os
import re
import csv

# fbfhTools.py: 自建的「出進口廠商管理系統」網頁的工具包
#   |- getCompanyBasic: 抓取某公司的基本資料
#   |- getCompanyGrade: 抓取某公司的近五年實績
#                       注意：不同年份的資料在合併時，要確認同欄位是否同年份
from fbfhTools import getCompanyBasic
from fbfhTools import getCompanyGrade

# 排除匯入的檔案
exclude = "outfiles/importedNumber.csv"

# 要匯入的檔案列表
infileList = []
for name in sys.argv:
    if re.search('[IE][0-9]{4}.+csv$', name):
        infileList.append(name)

# 要匯出的檔案與其參數
companyBasic = "outfiles" + os.path.sep + "CompanyBasic.csv"
companyGrade = "outfiles" + os.path.sep + "CompanyGrade.csv"
log          = "outfiles" + os.path.sep + "Log.csv"
columnsOfLog = 6
mode         = sys.argv[2] if len(sys.argv) > 2 else ""

# 抓取某csv檔的某欄位
def getColumn(infile, column, skipFirstRow):
    output = []
    with open(infile, 'r') as f:
        rows = csv.reader(f)
        if skipFirstRow:
            next(rows, None)
        for row in rows:
            output.append(row[column])
    return output


# 1. 新增空集合
numberList = set()

# 2. 把每個檔案抓出來的列表和 numberList 取聯集
for infile in infileList:
    new = set(getColumn(infile, 3, True))
    numberList = numberList.union(new)

# 3. 把 numberList 和 exclude 檔的列表取差集
if os.path.isfile(exclude):
    new = set(getColumn(exclude, 0, False))
    numberList = numberList.difference(new)

# 4. 匯出
with open(companyBasic, 'w') as f:
    for company in numberList:
        row = getCompanyBasic(company)
        if mode != "d":
            f.write(row + '\n')
        print(row)

with open(companyGrade, 'w') as f:
    for company in numberList:
        row = getCompanyGrade(company)
        if mode != "d":
            f.write(row + '\n')
        print(row)

with open(log, 'w') as f:
    for company in numberList:
        row = '"' + company + '"' + ',' * columnsOfLog
        if mode != "d":
            f.write(row + '\n')
        print(row)

'''
print(numberList)
print(len(numberList))
'''

