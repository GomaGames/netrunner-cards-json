'''
Converts all csv files in `csv_dir` to a dict, then writes all dicts as json to stdout.

Usage:

    python convert.py csvs > fnf.json

'''
import csv
import json
import os
import sys

if len(sys.argv) < 2:
    os.sys.stderr.write("Missing argument 'csv_dir'.\nUsage: python convert.py csv_dir\n")
    os.sys.exit(1)

csv_dir = sys.argv[1]
out = []

for c in os.listdir(csv_dir):
    file_path = os.path.join(csv_dir, c)
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # omit empty -------------------------------v
                out.append({k: v for k, v in row.items() if v})

out.sort(key=lambda k : k['code'])

print(json.dumps(out, indent=2))
