from csvTools import getColumn as getColumnFromCSV
from csvTools import makeCSV

# fbfhTools.py: 自建的「出進口廠商管理系統」網頁的工具包
#   |- getCompanyBasic: 抓取某公司的基本資料
from fbfhTools import getCompanyBasicV2 as getCompanyBasic


infile                  = "outfiles/importedFinal.csv"
infileLocateIDColumn    = 0
infileHasHeader         = False
outfile                 = "data/run4/companyBasic.csv"
method                  = getCompanyBasic
#columns                 = ['taxNumber', 'i109', 'e109', 'i108', 'e108', 'i107', 'e107', 'i106', 'e106', 'i105', 'e105']
columns                 = ['taxNumber', 'name', 'reg_date', 'address', 'phone']
includeHeader           = True
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
makeCSV(method, outfile, columns, rowIDs, includeHeader, showProgress)


