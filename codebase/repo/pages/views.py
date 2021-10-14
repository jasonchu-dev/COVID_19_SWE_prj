# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
import requests

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

def results(request):
    s1 = request.GET['search']
    return render(request,'results.html',{'search':s1})