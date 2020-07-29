import os
import fnmatch
import csv

infile = "."
category = "outfiles/category.csv"
cBasic   = "outfiles/cBasic.csv"
cGrade   = "outfiles/cGrade.csv"
logs     = "outfiles/logs.csv"

with open(category, "w") as f1, open(cBasic, "w") as f2, open(cGrade, "w") as f3, open(logs, "w") as f4:
    writer1 = csv.writer(f1)
    writer2 = csv.writer(f2)
    writer3 = csv.writer(f3)
    writer4 = csv.writer(f4)
    lines_seen = set()
    for filename in os.listdir(infile):
        if not fnmatch.fnmatch(filename, "*.csv"):
            continue
        with open(filename, newline='') as f:
            rows = csv.reader(f)
            next(rows, None)
            for row in rows:
                writer1.writerow(row[0:4])
                if row[3] not in lines_seen:
                    writer2.writerow(row[3:8])
                    writer3.writerow([row[3]] + row[8:])
                    writer4.writerow([row[3]])
                    lines_seen.add(row[3])
                print(row)
