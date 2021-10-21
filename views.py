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
    s2= ""
    # Opening JSON file (CHANGE THIS ON LOCAL PC)
    #(CHANGE PATH ON LOCAL PC!!)
    jsonFilePath = 'pages/demographics.json'
    input = request.GET['search']
    #function start
    # Opening JSON file 
    # file = open(jsonFilePath)
    
    # data = JSON object as list
    # data = json.load(file)
    
    # Iterating through the json
    # s2 = "{:<30}".format("demographic_category") + "demographic_value" + "administered_date" + "total_doses{:<30}" + "cumulative_total_doses{:<30}" + "pfizer_doses{:<30}" + "cumulative_pfizer_doses{:<30}" + "moderna_doses{:<30}" + "cumulative_moderna_doses{:<30}" + "jj_doses{:<30}" + "cumulative_jj_doses{:<30}" + "partially_vaccinated{:<30}" + "total_partially_vaccinated{:<30}" + "fully_vaccinated{:<30}" + "cumulative_fully_vaccinated{:<30}" + "at_least_one_dose{:<30}" + "cumulative_at_least_one_dose{:<30}\n"
    # s2 = "{:<30}".format("demographic_category") + "{:<30}".format("demographic_value")
    # s2 = (f"{'demographic_category':<30}{'demographic_value':<30}")

    # for i in data:
    #     if(input == i['demographic_value']):
    #         s2 = s2 + i['demographic_category'] + i['demographic_value'] + i['administered_date'] + str(i['total_doses']) + str(i['cumulative_total_doses']) + str(i['pfizer_doses']) + str(i['cumulative_pfizer_doses']) + str(i['moderna_doses']) + str(i['cumulative_moderna_doses']) + str(i['jj_doses']) + str(i['cumulative_jj_doses']) + str(i['partially_vaccinated']) + str(i['total_partially_vaccinated']) + str(i['fully_vaccinated']) + str(i['cumulative_fully_vaccinated']) + str(i['at_least_one_dose']) + str(i['cumulative_at_least_one_dose']) + '\n'
    #     elif(input == i['administered_date']):
    #         s2 = s2 + i['demographic_category'] + i['demographic_value'] + i['administered_date'] + str(i['total_doses']) + str(i['cumulative_total_doses']) + str(i['pfizer_doses']) + str(i['cumulative_pfizer_doses']) + str(i['moderna_doses']) + str(i['cumulative_moderna_doses']) + str(i['jj_doses']) + str(i['cumulative_jj_doses']) + str(i['partially_vaccinated']) + str(i['total_partially_vaccinated']) + str(i['fully_vaccinated']) + str(i['cumulative_fully_vaccinated']) + str(i['at_least_one_dose']) + str(i['cumulative_at_least_one_dose']) + '\n'
    #     elif(input == i['demographic_category']):
    #         s2 = s2 + i['demographic_category'] + i['demographic_value'] + i['administered_date'] + str(i['total_doses']) + str(i['cumulative_total_doses']) + str(i['pfizer_doses']) + str(i['cumulative_pfizer_doses']) + str(i['moderna_doses']) + str(i['cumulative_moderna_doses']) + str(i['jj_doses']) + str(i['cumulative_jj_doses']) + str(i['partially_vaccinated']) + str(i['total_partially_vaccinated']) + str(i['fully_vaccinated']) + str(i['cumulative_fully_vaccinated']) + str(i['at_least_one_dose']) + str(i['cumulative_at_least_one_dose']) + '\n'
        #else:
         #   s2 = "nothing found"
    # Closing file
    # file.close()
    return render(request,'results.html',{'search':s2})
