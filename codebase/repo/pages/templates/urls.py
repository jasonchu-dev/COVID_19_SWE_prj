# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, InsertPageView # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('insert/', InsertPageView.as_view(), name='insert'), 
    path('', HomePageView.as_view(), name='home'),  
    path('search/', views.results, name='search'),
]