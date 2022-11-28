import csv

# 抓取某csv檔的某欄位
def getColumn(infile, column, hasHeader = True):
    output = list()
    with open(infile, 'r') as f:
        rows = csv.reader(f)
        if hasHeader:
            next(rows, None)
        for row in rows:
            output.append(row[column]) 
    return output

def writeList(outfile, outlist):
    with open(outfile, 'w+') as f:
        for item in(outlist):
            f.write(item + '\n')
        

def makeCSV(method, outfile, columns, rowIDs, includeHeader = True, showProgress = True, filemode = 'w'):
    with open(outfile, filemode) as f:
        writer = csv.DictWriter(f, fieldnames = columns)
        if includeHeader:
            writer.writeheader()
        for i, rowID in enumerate(rowIDs):
            if showProgress:
                print(str(i) + ': ' + rowID)
            row = dict((k,v) for k, v in method(rowID).items() if k in columns)
            writer.writerow(row)
            if showProgress:
                print(row)

