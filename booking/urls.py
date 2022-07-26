from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('log/', views.loginPage, name='log'),
    path('registration/', views.registerPage, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
]