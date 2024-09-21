from django.contrib import  admin
from django.urls import path
    
from .views import CarAPI, FootballAPI, UfcAPI
    
urlpatterns=[
       path('carapi/', CarAPI.as_view()),
       path('carapi_v1/<int:pk>/', CarAPI.as_view()),
       path('footballapi/', FootballAPI.as_view()),
       path('footballapi_v2/<int:pk>/', FootballAPI.as_view()),
       path('ufcapi/', UfcAPI.as_view()),
       path('ufcapi_3/<int:pk>/', UfcAPI.as_view()),
]