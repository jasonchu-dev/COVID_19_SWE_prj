# pages/urls.py
from django.contrib import admin
from django.urls import path
from pages.views import race_vaccine_analytics
from pages.views import monthly_vaccination_analytics
from . import views
from .views import HomePageView, AboutPageView, InsertPageView, DeletePageView, AnalyticsPageView, Analytics2PageView # new


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),  
    path('search/', views.results, name='search'),
    path('delete/', DeletePageView.as_view(), name='delete'),
    path('delete/delete', views.delete_record, name='delete_results'),
    path('insert/', InsertPageView.as_view(), name='insert'), 
    path('insert/insert', views.insert_record, name='insert_results'), 
    path('insert/modify', views.modify_record, name='modify_results'), 
    path('backup/', views.backup_record, name='backup'), 
    path('admin/', admin.site.urls),
    path('analytics/', AnalyticsPageView.as_view(), name='analytics'), 
    path('analytics/monthlyVaccs', views.monthly_vaccination_analytics, name='analytics'),
    path('analytics/race', views.race_vaccine_analytics, name='analytics'),
    path('analytics/analytics2', Analytics2PageView.as_view(), name='analytics2'),
]