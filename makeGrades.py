import sys
from csvTools import getColumn as getColumnFromCSV
from csvTools import makeCSV

# fbfhTools.py: 自建的「出進口廠商管理系統」網頁的工具包
#   |- getCompanyGrade: 抓取某公司的近五年實績
#                       注意：不同年抓的資料在合併時，要確認同欄位是否同年份
from fbfhTools import getCompanyGradeV2 as getCompanyGrade

if len(sys.argv) < 3:
    exit("Usage: python concate.py [outfile] [infile]")

outfile = sys.argv[1]
infiles = sys.argv[2]

infile                  = sys.argv[1]
infileLocateIDColumn    = 0
infileHasHeader         = False
outfile                 = sys.argv[2]
method                  = getCompanyGrade
columns                 = ['taxNumber', 'i111', 'e111', 'i110', 'e110', 'i109', 'e109', 'i108', 'e108', 'i107', 'e107']
includeHeader           = False
showProgress            = True

print()
print(f"infile:                 '{infile}'")
print(f"infileHasHeader:        {infileHasHeader}")
print(f"infileLocateIDColumn:   {infileLocateIDColumn}")
print()
print(f"outfile:                '{outfile}'")
print(f"outfileHasHeader:       {includeHeader}")
print(f"columns:                {columns}")
print(f"method:                 {method}")
print()
print(f"showProgress:           {showProgress}")
print()

if input("enter 'y' to proceed: ") != 'y':
    exit('Abort.')

rowIDs          = set(getColumnFromCSV(infile, infileLocateIDColumn, infileHasHeader))
makeCSV(method, outfile, columns, rowIDs, includeHeader, showProgress, 'a')


