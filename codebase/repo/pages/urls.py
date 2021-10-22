# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, InsertPageView, DeletePageView# new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),  
    path('search/', views.results, name='search'),
    path('delete/', DeletePageView.as_view(), name='delete'),
    path('delete/delete', views.delete_record, name='delete_results'),
    path('insert/', InsertPageView.as_view(), name='insert'), 
    path('insert/insert', views.insert_record, name='insert_results'), #
    path('insert/modify', views.modify_record, name='modify_results'), #
]