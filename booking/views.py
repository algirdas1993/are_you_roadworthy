from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserAccount
# Create your views here.


def index(request):
    return render(request, 'booking/index.html')


def dashboard(request):
    return render(request, 'booking/dashboard.html')


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
    
    context = {}
    return render(request, 'booking/log.html', context)


def logOut(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = CreateUserAccount()

    if request.method == "POST":
        form = CreateUserAccount(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log')

    context = {'form': form}
    return render(request, 'booking/registration.html', context)