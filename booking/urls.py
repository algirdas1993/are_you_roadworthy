from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index),
    path('log/', views.log),
    path('registration/', views.registerPage),
]