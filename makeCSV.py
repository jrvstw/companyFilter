import sys
import os
import re
import csv

# fbfhTools.py: 自建的「出進口廠商管理系統」網頁的工具包
#   |- getCompanyBasic: 抓取某公司的基本資料
#   |- getCompanyGrade: 抓取某公司的近五年實績
#                       注意：不同年抓的資料在合併時，要確認同欄位是否同年份
from fbfhTools import getCompanyBasicV2 as getCompanyBasic
from fbfhTools import getCompanyGradeV2 as getCompanyGrade

# 抓取某csv檔的某欄位
def getColumnFromCSV(infile, column, skipFirstRow):
    output = []
    with open(infile, 'r') as f:
        rows = csv.reader(f)
        if skipFirstRow:
            next(rows, None)
        for row in rows:
            output.append(row[column])
    return output

def makeCSV(outfile, columns, rowIDs, method, hasHeader, showProgress):
    with open(outfile, 'w') as f:
        writer = csv.DictWriter(f, fieldnames = columns)
        if hasHeader:
            writer.writeheader()
        for i, rowID in enumerate(rowIDs):
            if showProgress:
                print(str(i) + ': ' + rowID)
            row = dict((k,v) for k, v in method(rowID).items() if k in columns)
            writer.writerow(row)
            if showProgress:
                print(row)


infile                  = "outfiles/toImport.csv"
infileLocateIDColumn    = 0
infileHasHeader         = False
outfile                 = "outfiles/companyBasic2.csv"
method                  = getCompanyBasic
#columns                 = ['taxNumber', 'i109', 'e109', 'i108', 'e108', 'i107', 'e107', 'i106', 'e106', 'i105', 'e105']
columns                 = ['taxNumber', 'name', 'reg_date', 'address', 'phone']
outfileHasHeader        = True
showProgress            = True

print()
print(f"infile:                 '{infile}'")
print(f"infileHasHeader:        {infileHasHeader}")
print(f"infileLocateIDColumn:   {infileLocateIDColumn}")
print()
print(f"outfile:                '{outfile}'")
print(f"outfileHasHeader:       {outfileHasHeader}")
print(f"columns:                {columns}")
print(f"method:                 {method}")
print()
print(f"showProgress:           {showProgress}")
print()

if input("enter 'y' to proceed: ") != 'y':
    exit('Abort.')

rowIDs          = set(getColumnFromCSV(infile, infileLocateIDColumn, infileHasHeader))
makeCSV(outfile, columns, rowIDs, method, outfileHasHeader, showProgress)


