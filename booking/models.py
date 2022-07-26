from django.db import models


# Create your models here.

class BookingTime(models.Model):
    car_reg_number = models.CharField(max_length=6, null=True)
    check_date_time = models.DateTimeField(null=True, unique=True)
    # check_time = models.TimeField()

    def __str__(self):
        return self.name


