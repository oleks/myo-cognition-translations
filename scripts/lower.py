#!/usr/bin/env python3

import csv
import string
import tempfile
import os

def process_csv(out_file, in_file_path):
    with open(in_file_path, 'r', encoding='utf-8') as in_file:
        reader = csv.reader(in_file)
        writer = csv.writer(
            out_file,
            delimiter=',',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')
        writer.writerow(next(reader))
        for row in reader:
            if row[1].lower() == row[1] and not row[2].lower() == row[2]:
                row[2] = row[2].lower()
            writer.writerow(row)

out_file = tempfile.NamedTemporaryFile(
    mode='w',
    delete=False,
    encoding='utf-8',
    dir='.')
in_file_path = 'MyoCognitionDictonary.csv'
try:
    process_csv(out_file, in_file_path)
    out_file.close()
    os.rename(out_file.name, in_file_path)
except Exception as e:
    print("fail", str(e))
    out_file.close()
    os.remove(out_file.name)
