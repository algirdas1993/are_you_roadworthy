from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserAccount, CreateBookingTime
from .models import BookingTime
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='/log')
def bookingTime(request):
    form = CreateBookingTime()

    if request.method == 'POST':
        form = CreateBookingTime(request.POST)
        if form.is_valid():
            form.save()
        return redirect('bookings')

    context = {'form': form}
    return render(request, 'booking/form.html', context)


@login_required(login_url='/log')
def updateBooking(request, pk):
    booking = BookingTime.objects.get(car_reg_number=pk)
    form = CreateBookingTime(instance=booking)

    if request.method == 'POST':
        form = CreateBookingTime(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')

    context = {'form': form}
    return render(request, 'booking/form.html', context)


@login_required(login_url='/log')
def deleteBooking(request, pk):
    booking = BookingTime.objects.get(car_reg_number=pk)

    if request.method == 'POST':
        booking.delete()
        return redirect('bookings')
    return render(request, 'booking/delete.html', {'object': booking})


@login_required(login_url='/log')
def bookings(request):
    bookings = BookingTime.objects.all().values()
    context = {'bookings': bookings}
    return render(request, 'booking/bookings.html', context)