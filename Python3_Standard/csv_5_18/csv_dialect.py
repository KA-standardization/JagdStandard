import csv

print(csv.list_dialects())
print('=' * 88)

csv.register_dialect('pipes', delimiter='|')
with open('testdata2.csv', 'r') as f:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        print(row)
