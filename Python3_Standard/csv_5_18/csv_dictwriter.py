import csv

filenames = ('q1', 'q2', 'q3')
header = {n: n for n in filenames}

with open('testdata3.csv', 'wt') as f:
    writer = csv.DictWriter(f, fieldnames=filenames)
    writer.writeheader()

    for i in range(3):
        writer.writerow({'q1': i, 'q2': i + 2, 'q3': i + 4})
