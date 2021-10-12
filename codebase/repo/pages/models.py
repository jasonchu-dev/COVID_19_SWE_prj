from django.db import models

# Create your models here.

# importing csv module
import csv
  
# csv file name
filename = "c19demographics.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the column names
print('Field names are:' + ', '.join(field for field in fields))

#total of 17 fields below: 
#demographic_category | demographic_value | administered_date | total_doses | cumulative_total_doses 
#pfizer_doses | cumulative_pfizer_doses | moderna_doses | cumulative_moderna_doses | jj_doses 
#cumulative_jj_doses | partially_vaccinated | total_partially_vaccinated | fully_vaccinated
#cumulative_fully_vaccinated | at_least_one_dose | cumulative_at_least_one_dose

#  printing first 5 rows
print('\nFirst 5 rows :\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')

##References:
#https://www.geeksforgeeks.org/working-csv-files-python/