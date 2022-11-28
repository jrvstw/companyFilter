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
    