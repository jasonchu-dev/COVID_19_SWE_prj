from django.db import models

# Create your models here.

# importing csv and json module
import csv
import json
  
# initializing the rows list
rows = []
  
# reading csv file
with open("c19demographics.csv", "r") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

with open("c19demographics.json", "w") as jsonfile:
    jsonfile.write(json.dumps(rows, indent=3))