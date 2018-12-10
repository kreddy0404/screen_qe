import csv
import math
from collections import defaultdict
from glob import glob, iglob
from itertools import chain


def avg(path):
    total = 0

    for i, f in enumerate(iglob('{}/**/*.csv'.format(path), recursive=True)):
        with open(f, 'rb') as fh:
            total += next(fh).decode('utf8', errors='ignore').count(',')

    print(math.ceil(total / i))


def word_count(path):
    coll = defaultdict(int)

    for _, f in enumerate(iglob('{}/**/*.csv'.format(path), recursive=True)):
        with open(f, 'rb') as fh:
            lines = list(chain.from_iterable([l.decode('utf8', errors='ignore').split(',') for l in fh.readlines()]))
            for k in lines:
                coll[k] += 1

    with open('wordcound.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['value', 'count'])
        writer.writeheader()
        for k in coll:
            writer.writerow({'value': k, 'count': coll[k]})


def row_count(path):
    lines = 0

    for f in glob('{}/**/*.csv'.format(path), recursive=True):
        with open(f, 'rb') as fh:
            lines += len(fh.readlines())

    print(lines)


def all(path):
    for f in [avg, word_count, row_count]:
        f(path)
