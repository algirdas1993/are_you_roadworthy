from django.contrib import admin

# Register your models here.

from .models import BookingTime


admin.site.register(BookingTime)