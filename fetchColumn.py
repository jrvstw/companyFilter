import csv

input_file = 'infiles/taxSheet.csv'
fetch_column = 5
output_file = 'outfiles/taxNumberList.csv'

array = []
with open(input_file, newline='') as infile:
    rows = csv.reader(infile)
    for row in rows:
        if row[fetch_column - 1]:
            array.append(row[fetch_column - 1].zfill(8))

#print(array)
with open(output_file, 'w') as outfile:
    for number in array:
        outfile.write(number + '\n')

