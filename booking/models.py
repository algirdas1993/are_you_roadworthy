from django.db import models


# Create your models here.

class BookingTime(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    car_reg_number = models.CharField(max_length=6, null=True)
    check_date_time = models.DateTimeField(null=True, unique=True)
    # check_time = models.TimeField()


    def __str__(self):
        return self.name

   
