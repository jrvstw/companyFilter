from csvTools import getColumn

exclude = "outfiles/importedCategory.csv"
outfile = "outfiles/run4i.sh"

excludeList = set(getColumn(exclude, 0, False))

with open(outfile, 'w') as f:
    for i in range(100, 10000):
        category = 'I' + str(i).zfill(4)
        if category not in excludeList:
            f.write("python fetch.py " + category + " y\n")

