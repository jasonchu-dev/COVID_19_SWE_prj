import json
import csv

rows = []

with open ("covid19vaccinesadministeredbydemographics.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        rows.append(row)

with open ("covid19vaccinesadministeredbydemographics.json", "w") as jsonfile:
    jsonfile.write(json.dumps(rows, indent=3))