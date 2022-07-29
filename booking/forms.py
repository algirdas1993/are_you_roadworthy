from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import BookingTime


class CreateUserAccount(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateBookingTime(ModelForm):
    class Meta:
        model = BookingTime
        fields = '__all__'
