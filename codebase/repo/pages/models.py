from django.db import models

# Create your models here.

# importing csv and json module
import csv
import json 

# reading csv file
with open("c19demographics.csv", "r") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # initializing the info list
    info = {"key": []} # problem here

    # go to next line (skip titles)
    next(csvreader)
    
    # extracting each data row one by one
    for row in csvreader:
        info["key"].append # problem here
        (
            {
                "county": row[0],
                "administered date": row[1]
            }
        )
        #info.append(row)

with open("c19demographics.json", "w") as jsonfile:
    jsonfile.write(json.dumps(info, indent=3))



#reading other csv file
with open("c19county.csv", "r") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    #clear info for next set
    info = {"key": []} # problem here

    # go to next line (skip titles)
    next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        info["key"].append # problem here
        (
            {
                "demographic category" : row[0],
                "demographic value" : row[1]
            }
        )
        #info.append(row)

with open("c19county.json", "w") as jsonfile:
    jsonfile.write(json.dumps(info, indent=3))