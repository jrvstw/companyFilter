import sys
from multitaskTools import concateFiles

if len(sys.argv) < 3:
    exit("Usage: python concate.py [outfile] [infiles]+")

outfile = sys.argv[1]
infiles = sys.argv[2:]

concateFiles(outfile, infiles)

