# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, VaccineSearchView # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),  
    path('', VaccineSearchView.as_view(), name='search'),  
]