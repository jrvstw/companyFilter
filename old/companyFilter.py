import csv

database_file = 'infiles/companyData.csv'
filter_list = 'outfiles/taxNumberList.csv'
output_file = 'outfiles/companyMatch.csv'

numberlist = []
with open(filter_list, newline='') as infile:
    rows = csv.reader(infile)
    for row in rows:
        numberlist.append(row[0])

#print(numberlist)

with open(output_file, 'w') as outfile:
    with open(database_file, 'r') as infile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if row[0].zfill(8) in numberlist:
                writer.writerow(row)


