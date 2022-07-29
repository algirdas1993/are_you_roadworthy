from django.contrib import admin

# Register your models here.

from .models import BookingTime, Review


admin.site.register(BookingTime)
admin.site.register(Review)