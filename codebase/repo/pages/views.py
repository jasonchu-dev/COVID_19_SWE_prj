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
    jsonFilePath = '/Users/brayanmontiel/Documents/UCR/2021--CURRENT/FALL 2021/CS180/codebase/project-main/cs180project-022-cs180ucrejects/codebase/repo/pages/demographics.json'
    f = open(jsonFilePath)
    # data = JSON object as list
    data = json.load(f)
    s2 = ''
    # Iterating through the json
    for i in data:
        if s1 == i['demographic_category']:
            s2+= i['demographic_value']
            s2+= ' '
            s2+= i['administered_date']
            s2+= ' '
            s2+= str(i['total_doses'])
            s2+= ' '
            s2+= str(i['cumulative_total_doses'])
            s2+= ' '
            s2+= str(i['pfizer_doses'])
            s2+= ' '
            s2+= str(i['cumulative_pfizer_doses'])
            s2+= ' '
            s2+= str(i['moderna_doses'])
            s2+= ' '
            s2+= str(i['cumulative_moderna_doses'])
            s2+= ' '
            s2+= str(i['jj_doses'])
            s2+= ' '
            s2+= str(i['cumulative_jj_doses'])
            s2+= ' '
            s2+= str(i['partially_vaccinated'])
            s2+= ' '
            s2+= str(i['total_partially_vaccinated'])
            s2+= ' '
            s2+= str(i['fully_vaccinated'])
            s2+= ' '
            s2+= str(i['cumulative_fully_vaccinated'])
            s2+= ' '
            s2+= str(i['at_least_one_dose'])
            s2+= ' '
            s2+= str(i['cumulative_at_least_one_dose'])
            s2+= '\n'
        else:
            s2 = 'No results...try again.'
    # Closing file
    f.close()
    return render(request,'results.html',{'search':s2})
