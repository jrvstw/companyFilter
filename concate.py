import sys

def concateFiles(outfile, infiles, skipFirstRow = True, showProgress = True):
    fo = open(outfile, 'w')
    for infile in infiles:
        fi = open(infile, 'r')
        if skipFirstRow:
            fi.readline()
        content = fi.read()
        fo.write(content)
        if showProgress:
            print(content)
        fi.close()
    fo.close()

if len(sys.argv) < 3:
    exit("Usage: python concate.py [outfile] [infiles]+")

outfile = sys.argv[1]
infiles = sys.argv[2:]

concateFiles(outfile, infiles)

