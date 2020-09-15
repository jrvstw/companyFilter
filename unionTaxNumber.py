import sys
import os
import re
import csv

from csvTools import getColumn as getColumnFromCSV
from csvTools import makeCSV

outfile = "outfiles/imported4a.csv"
# 排除匯入的統編清單
excludeList = [
        "outfiles/imported2.csv",
        "outfiles/imported3.csv",
        ]

# 要匯入的檔案
infileList = []
for name in sys.argv[1:]:
    if re.search('[IE][0-9]{4}.+csv$', name):
        infileList.append(name)



# 1. 把每個檔案抓出來的列表取聯集
numberList = set()
for infile in infileList:
    new = set(getColumnFromCSV(infile, 3, True))
    numberList = numberList.union(new)

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
'''
print(len(numberList))
# 2. 把 numberList 和 exclude 檔的列表取差集
for exfile in excludeList:
    new = set(getColumnFromCSV(exfile, 0, False))
    numberList = numberList.difference(new)


makeCSV(
        method        = lambda number : {"tax number": f"{number}"},
        outfile       = outfile,
        columns       = ["tax number"],
        rowIDs        = numberList,
        includeHeader = False,
        showProgress  = True,
        )

'''

