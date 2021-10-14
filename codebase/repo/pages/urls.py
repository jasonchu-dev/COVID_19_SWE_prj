# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),  
    path('search/', views.results, name='search'),
]