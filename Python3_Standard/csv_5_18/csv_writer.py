import sys
import csv

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(('t1', 't2', 't3'))
    for i in range(3):
        row = (i, i + 1, i + 2)
        writer.writerow(row)
