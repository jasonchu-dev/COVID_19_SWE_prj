# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json

#Load json into array data
jsonFilePath = 'pages/demographics.json'
f = open(jsonFilePath)
#elements of json file will be in array: data#
data = json.load(f)
f.close()

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class DeletePageView(TemplateView): 
    template_name = 'delete.html'
class InsertPageView(TemplateView):
    template_name = 'insert.html'



def results(request):
    s1 = request.GET['search']
    # Opening JSON file (CHANGE THIS ON LOCAL PC)
    #(CHANGE PATH ON LOCAL PC!!)
    jsonFilePath = 'pages/demographics.json'
    input = request.GET['search']
    #function start
    s2= ""
    # Opening JSON file 
    f = open(jsonFilePath)
    
    # data = JSON object as list
    data = json.load(f)
    
    # Iterating through the json
    s2 = "demographic_category " + "demographic_value " + "administered_date " + "total_doses " + "cumulative_total_doses " + "pfizer_doses " + "cumulative_pfizer_doses " + "moderna_doses " + "cumulative_moderna_doses " + "jj_doses " + "cumulative_jj_doses " + "partially_vaccinated " + "total_partially_vaccinated " + "fully_vaccinated " + "cumulative_fully_vaccinated " + "at_least_one_dose "+ "cumulative_at_least_one_dose\n"

#search method
def results(request):
    input = request.GET['search'] #retrieves the GET for search
    s2= '' #will be our return string
    for i in data:
        if input == i['demographic_value'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
        elif input == i['administered_date'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
        elif input == i['demographic_category'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
        elif input == str(i['ID']) :
            s2 = str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
            break
    if s2 == '': #basically if empty then no search found
        s2 = "No matching results...pleast try again."
    return render(request,'results.html',{'search':s2})

#delte method
def delete_record(request):
    input = request.GET['delete'] #retrieves the GET for deleting
    s3= '' #will be our return string
    for i in data:
        if input == str(i['ID']) : #this works in terms of getting it to 'delete' everytime surver runs 
            i['ID'] = 0         #will not show up in GUI anymore...back end still needs to fix to update json
            i['demographic_category'] = 0
            i['demographic_value']  = 0
            i['administered_date'] = 0
            i['total_doses'] = 0
            i['cumulative_total_doses'] = 0
            i['pfizer_doses'] = 0
            i['cumulative_pfizer_doses'] = 0
            i['moderna_doses'] = 0
            i['cumulative_moderna_doses'] = 0 
            i['jj_doses'] = 0
            i['cumulative_jj_doses'] = 0 
            i['partially_vaccinated'] = 0 
            i['total_partially_vaccinated'] = 0 
            i['fully_vaccinated'] = 0 
            i['cumulative_fully_vaccinated'] = 0 
            i['at_least_one_dose'] = 0 
            i['cumulative_at_least_one_dose'] = 0
            s3 = 'Success. Entry record #' + input + ' has been deleted.'
            break
        elif input != str(i['ID']) :
            s3 = 'Record not found. Please try again.'
    return render(request,'delete.html',{'delete':s3})

