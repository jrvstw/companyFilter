import sys
import os
import re
import csv

# 排除匯入的統編清單
exclude = "outfiles/imported.csv"
outfile = "outfiles/toImport.csv"

# 要匯入的檔案
infileList = []
for name in sys.argv[1:]:
    if re.search('[IE][0-9]{4}.+csv$', name):
        infileList.append(name)

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



# 1. 把每個檔案抓出來的列表取聯集
numberList = set()
for infile in infileList:
    new = set(getColumn(infile, 3, True))
    numberList = numberList.union(new)

# 2. 把 numberList 和 exclude 檔的列表取差集
if os.path.isfile(exclude):
    new = set(getColumn(exclude, 0, False))
    numberList = numberList.difference(new)

# 3. 匯出
def myExport(table, method, outfile, mode):
    with open(outfile, 'w') as f:
        for row in table:
            content = method(row)
            if mode != 'd':
                f.write(content + '\n')
            print(content)

def getNumberList(number):
    return f'{number}'

myExport(numberList, getNumberList, outfile, '')

