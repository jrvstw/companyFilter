import sys
import os
import re
import csv

# fbfhTools.py: 自建的「出進口廠商管理系統」網頁的工具包
#   |- getCompanyBasic: 抓取某公司的基本資料
#   |- getCompanyGrade: 抓取某公司的近五年實績
#                       注意：不同年抓的資料在合併時，要確認同欄位是否同年份
from fbfhTools import getCompanyBasic
from fbfhTools import getCompanyGrade


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


infile = 'data/run1/joindate.csv'
outfile = 'data/run1/joindate2.csv'

with open(outfile, 'w') as fo:
    writer = csv.writer(fo)
    with open(infile, newline='') as fi:
        rows = csv.reader(fi)
        for row in rows:
            date = row[5].split('/')
            date[0] = str(int(date[0]) + 1911)
            row[5] = '-'.join(date)
            writer.writerow(row)

