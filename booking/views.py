from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserAccount
# Create your views here.


def index(request):
    return render(request, 'booking/index.html')


def log(request):
    return render(request, 'booking/log.html')


def registerPage(request):
    form = CreateUserAccount()

    if request.method == "POST":
        form = CreateUserAccount(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'booking/registration.html', context)