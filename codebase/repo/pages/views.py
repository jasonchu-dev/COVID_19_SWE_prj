# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

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

    for i in data:
        if(input == i['demographic_value']):
            s2 = s2 + i['demographic_category'] + i['demographic_value'] + i['administered_date'] + str(i['total_doses']) + str(i['cumulative_total_doses']) + str(i['pfizer_doses']) + str(i['cumulative_pfizer_doses']) + str(i['moderna_doses']) + str(i['cumulative_moderna_doses']) + str(i['jj_doses']) + str(i['cumulative_jj_doses']) + str(i['partially_vaccinated']) + str(i['total_partially_vaccinated']) + str(i['fully_vaccinated']) + str(i['cumulative_fully_vaccinated']) + str(i['at_least_one_dose']) + str(i['cumulative_at_least_one_dose']) + '\n'
        elif(input == i['administered_date']):
            s2 = s2 + i['demographic_category'] + i['demographic_value'] + i['administered_date'] + str(i['total_doses']) + str(i['cumulative_total_doses']) + str(i['pfizer_doses']) + str(i['cumulative_pfizer_doses']) + str(i['moderna_doses']) + str(i['cumulative_moderna_doses']) + str(i['jj_doses']) + str(i['cumulative_jj_doses']) + str(i['partially_vaccinated']) + str(i['total_partially_vaccinated']) + str(i['fully_vaccinated']) + str(i['cumulative_fully_vaccinated']) + str(i['at_least_one_dose']) + str(i['cumulative_at_least_one_dose']) + '\n'
        elif(input == i['demographic_category']):
            s2 = s2 + i['demographic_category'] + i['demographic_value'] + i['administered_date'] + str(i['total_doses']) + str(i['cumulative_total_doses']) + str(i['pfizer_doses']) + str(i['cumulative_pfizer_doses']) + str(i['moderna_doses']) + str(i['cumulative_moderna_doses']) + str(i['jj_doses']) + str(i['cumulative_jj_doses']) + str(i['partially_vaccinated']) + str(i['total_partially_vaccinated']) + str(i['fully_vaccinated']) + str(i['cumulative_fully_vaccinated']) + str(i['at_least_one_dose']) + str(i['cumulative_at_least_one_dose']) + '\n'
        #else:
         #   s2 = "nothing found"
    # Closing file
    f.close()
    return render(request,'results.html',{'search':s2})
