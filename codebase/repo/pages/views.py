# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

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
    s2 = "demographic_category{:<30}" + "demographic_value{:<30}" + "administered_date{:<30}" + "total_doses{:<30}" + "cumulative_total_doses{:<30}" + "pfizer_doses{:<30}" + "cumulative_pfizer_doses{:<30}" + "moderna_doses{:<30}" + "cumulative_moderna_doses{:<30}" + "jj_doses{:<30}" + "cumulative_jj_doses{:<30}" + "partially_vaccinated{:<30}" + "total_partially_vaccinated{:<30}" + "fully_vaccinated{:<30}" + "cumulative_fully_vaccinated{:<30}" + "at_least_one_dose{:<30}" + "cumulative_at_least_one_dose{:<30}\n"

    for i in data:
        if(input == i['demographic_value']):
            s2 = s2 + i['demographic_category{:<30}'] + i['demographic_value{:<30}'] + i['administered_date{:<30}'] + str(i['total_doses{:<30}']) + str(i['cumulative_total_doses{:<30}']) + str(i['pfizer_doses{:<30}']) + str(i['cumulative_pfizer_doses{:<30}']) + str(i['moderna_doses{:<30}']) + str(i['cumulative_moderna_doses{:<30}']) + str(i['jj_doses{:<30}']) + str(i['cumulative_jj_doses{:<30}']) + str(i['partially_vaccinated{:<30}']) + str(i['total_partially_vaccinated{:<30}']) + str(i['fully_vaccinated{:<30}']) + str(i['cumulative_fully_vaccinated{:<30}']) + str(i['at_least_one_dose{:<30}']) + str(i['cumulative_at_least_one_dose{:<30}']) + '\n'
        elif(input == i['administered_date']):
            s2 = s2 + i['demographic_category{:<30}'] + i['demographic_value{:<30}'] + i['administered_date{:<30}'] + str(i['total_doses{:<30}']) + str(i['cumulative_total_doses{:<30}']) + str(i['pfizer_doses{:<30}']) + str(i['cumulative_pfizer_doses{:<30}']) + str(i['moderna_doses{:<30}']) + str(i['cumulative_moderna_doses{:<30}']) + str(i['jj_doses{:<30}']) + str(i['cumulative_jj_doses{:<30}']) + str(i['partially_vaccinated{:<30}']) + str(i['total_partially_vaccinated{:<30}']) + str(i['fully_vaccinated{:<30}']) + str(i['cumulative_fully_vaccinated{:<30}']) + str(i['at_least_one_dose{:<30}']) + str(i['cumulative_at_least_one_dose{:<30}']) + '\n'
        elif(input == i['demographic_category']):
            s2 = s2 + i['demographic_category{:<30}'] + i['demographic_value{:<30}'] + i['administered_date{:<30}'] + str(i['total_doses{:<30}']) + str(i['cumulative_total_doses{:<30}']) + str(i['pfizer_doses{:<30}']) + str(i['cumulative_pfizer_doses{:<30}']) + str(i['moderna_doses{:<30}']) + str(i['cumulative_moderna_doses{:<30}']) + str(i['jj_doses{:<30}']) + str(i['cumulative_jj_doses{:<30}']) + str(i['partially_vaccinated{:<30}']) + str(i['total_partially_vaccinated{:<30}']) + str(i['fully_vaccinated{:<30}']) + str(i['cumulative_fully_vaccinated{:<30}']) + str(i['at_least_one_dose{:<30}']) + str(i['cumulative_at_least_one_dose{:<30}']) + '\n'
        #else:
         #   s2 = "nothing found"
    # Closing file
    f.close()
    return render(request,'results.html',{'search':s2})
