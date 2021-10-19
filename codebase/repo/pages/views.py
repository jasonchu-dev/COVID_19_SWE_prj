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

#search method
def results(request):
    input = request.GET['search'] #retrieves the GET for search
    s2= "" #will be our return string
    for i in data:
        if input == i['demographic_value'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '\n'
        elif input == i['administered_date'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '\n'
        elif input == i['demographic_category'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '\n'
        elif input == str(i['ID']) :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '\n'
        #else: 
        #    s2 = "No matching results...pleast try again."
    return render(request,'results.html',{'search':s2})

#delte method
def delete_record(request):
    input = request.GET['delete'] #retrieves the GET for deleting
    s3= '' #will be our return string
    for i in data:
        if input == i['ID'] :
            del data[i]
            s3 = 'Success. Entry ' + input + ' has been deleted.'
        else:
            s3 = 'Record not found. Please try again.'
        #    s2 = "No matching results...pleast try again."
    return render(request,'delete.html',{'delete':s3})
