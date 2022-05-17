import csv

with open('testdata.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
