import sys
from csvTools import getColumn as getColumnFromCSV
from csvTools import writeList

if len(sys.argv) < 4:
    exit("Usage: python concate.py [outfile] [infile] [#column]")

outfile = sys.argv[1]
infile  = sys.argv[2]
column  = int(sys.argv[3])

output = getColumnFromCSV(infile, column, False)
writeList(outfile, output)
