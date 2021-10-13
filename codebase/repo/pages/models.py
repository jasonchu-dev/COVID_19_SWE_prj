from django.db import models
import os
import json

# Create your models here.

#backup way
#info = []
#with open (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'demographics.csv'), 'r') as csvfile:
#    with open ("demographics.json", 'w') as jsonfile:
#        for row in csvfile:
 #           info = row.split(',')
 #           jsonfile.write(' '.join(info))

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        for line in csvf:
            words = line.split(',')
            jsonArray.append((words[0], words[1:]))
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'demographics.csv'
jsonFilePath = r'demographics.json'
csv_to_json(csvFilePath, jsonFilePath)