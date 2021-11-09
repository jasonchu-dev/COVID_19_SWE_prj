# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView ,IncrementPageView # new
# new

from pages.views import increment_analytics
urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),  
    path('search/', views.results, name='search'),
    path('Increment/', IncrementPageView.as_view(), name='increment'),
    path('Increment/monthlyIncrement', views.increment_analytics , name='increment')
]
