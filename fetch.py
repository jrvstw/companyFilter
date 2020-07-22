import sys
import os
import myfunctions as mf

(ieType, ccc) = mf.validate(sys.argv)
(pagesCount, companiesCount) = mf.getCounts(ieType, ccc)
outfile  = ieType + ccc + "(" + str(companiesCount) + ").csv"

print('Saving ' + str(companiesCount) + ' items to "' + outfile + '".')
'''
if input('Enter "y" to proceed: ') != "y":
    exit("Abort.")
    '''

with open(outfile, 'w') as f:
    header = '"I/E",ccc,serial,"tax number",name,area,address,phone,109i,109e,108i,108e,107i,107e,106i,106e,105i,105e\n'
    f.write(header)
    for page in range(pagesCount):
        table = mf.getTable(ieType, ccc, page)
        for index, company in enumerate(table):
            row = mf.getRow(ieType, ccc, page, index, company)
            f.write(row + '\n')
            print(row)

