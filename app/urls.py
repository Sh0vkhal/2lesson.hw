from django.contrib import  admin
from django.urls import path
    
from .views import CarAPI, FootballAPI, UfcAPI
    
urlpatterns=[
        path('carapi/', CarAPI.as_view()),
        path('footballapi/', FootballAPI.as_view()),
        path('ufcapi/', UfcAPI.as_view()),
    ]