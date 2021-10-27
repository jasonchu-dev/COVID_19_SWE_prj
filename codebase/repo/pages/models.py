from django.db import models
import os
import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO


#creating get_graph dependencies, converting to utf-8
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,5))
    plt.title('Vaccination rates by Demographics')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Gender')
    plt.ylabel('Vaccinations')
    plt.tight_layout()
    graph = get_graph()
    return graph

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
          
def search_json_file(jsonFilePath):
    # Opening JSON file (CHANGE THIS ON LOCAL PC)
    f = open(jsonFilePath)
    
    # data = JSON object as list
    data = json.load(f)
    
    # Iterating through the json
    for i in data:
        print(i['ID'])
    
    # Closing file
    f.close()



#(CHANGE PATH ON LOCAL PC!!)
csvFilePath = '/Users/brayanmontiel/Documents/UCR/2021--CURRENT/FALL 2021/CS180/codebase/project-main/cs180project-022-cs180ucrejects/codebase/repo/pages/demographics.csv'
#correctly parsed json file 
jsonFilePath = '/Users/brayanmontiel/Documents/UCR/2021--CURRENT/FALL 2021/CS180/codebase/project-main/cs180project-022-cs180ucrejects/codebase/repo/pages/demographics.json' 

#method calls:
#csv_to_json(csvFilePath, jsonFilePath) #only needed to create json once
#search_json_file(jsonFilePath)