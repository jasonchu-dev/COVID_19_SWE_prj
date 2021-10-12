# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class VaccineSearchView(TemplateView): # new
    template_name = 'search_vaccines.html'