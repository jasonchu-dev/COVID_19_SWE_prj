from django.db import models

# Create your models here.

# importing csv and json module
import csv
import json 

# reading csv file
with open("c19demographics.csv", "r") as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)

    with open("c19demographics.json", "w") as jsonfile:
        fieldnames = [
            'demographic_category',
            'demographic_value',
            'administered_date',
            'total_doses',
            'cumulative_total_doses',
            'pfizer_doses',
            'cumulative_pfizer_doses',
            'moderna_doses',
            'cumulative_moderna_doses',
            'jj_doses',
            'cumulative_jj_doses',
            'partially_vaccinated',
            'total_partially_vaccinated',
            'fully_vaccinated',
            'cumulative_fully_vaccinated',
            'at_least_one_dose',
            'cumulative_at_least_one_dose'
        ]
        jsonwriter = csv.DictWriter(jsonfile, fieldnames=fieldnames, delimiter='\t')
        
        jsonwriter.writeheader()

        for row in csvreader:
            jsonwriter.writerow(row)



# # old code
# #reading other csv file
# with open("c19county.csv", "r") as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
      
#     #clear info for next set
#     info = {"key": []} # problem here

#     # go to next line (skip titles)
#     next(csvreader)
  
#     # extracting each data row one by one
#     for row in csvreader:
#         info["key"].append # problem here
#         (
#             {
#                 "demographic category" : row[0],
#                 "demographic value" : row[1]
#             }
#         )
#         #info.append(row)

# with open("c19county.json", "w") as jsonfile:
#     jsonfile.write(json.dumps(info, indent=3))