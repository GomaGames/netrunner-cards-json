'''
Converts all csv files in `csv_dir` to a dict, then writes all dicts as json to stdout.

Usage:

    python convert.py csvs > fnf.json

'''
import csv
import json
import os
import sys

if len(sys.argv) < 3:
    os.sys.stderr.write("Missing arguments.\nUsage: python convert.py csv_path json_path\n")
    os.sys.exit(1)

csv_path = sys.argv[1]
json_path = sys.argv[2]
out = []

if os.path.isfile(csv_path):
    with open(csv_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # omit empty -------------------------------v
            out.append({k: v for k, v in row.items() if v})

out.sort(key=lambda k : k['code'])

with open(json_path, "w") as file:
    file.write(json.dumps(out, indent=2))

print("Wrote json to %s" % json_path)
