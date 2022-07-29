from django.db import models
from django.contrib.auth.decorators import login_required


# Create your models here.

class BookingTime(models.Model):

    class Meta:
        unique_together = ('car_reg_number', 'check_date', 'check_time')

    TIME_CHOICES = (
        (0, '07:00 - 07:30'),
        (1, '07:30 - 08:00'),
        (2, '08:00 - 08:30'),
        (3, '08:30 - 09:00'),
        (4, '09:00 - 09:30'),
        (5, '09:30 - 10:00'),
        (6, '10:00 - 10:30'),
        (7, '10:30 - 11:00'),
        (8, '11:00 - 11:30'),
        (9, '11:30 - 12:00'),
        (10, '12:00 - 12:30'),
        (11, '12:30 - 13:00'),
        (12, '13:00 - 13:30'),
        (13, '13:30 - 14:00'),
        (14, '14:00 - 14:30'),
        (15, '14:30 - 15:00'),
        (16, '15:00 - 15:30'),
        (17, '15:30 - 16:00'),
        (18, '16:00 - 16:30'),
        (19, '16:30 - 17:00'),
        (20, '17:00 - 17:30'),
        (21, '17:30 - 18:00'),
        (22, '18:00 - 18:30'),
        (23, '18:30 - 19:00'),

    )

    SERVICE_CHOICES = (
        (0, 'NO EXTRA SERVICE'),
        (1, 'SEFETY INSPECTION'),
        (2, 'SEFETY INSPECTION +PLUS'),
        (3, 'COMPLETE SEFETY INSPECTION'),
    )   

    car_reg_number = models.CharField(max_length=6, default=True, primary_key=True)
    check_date = models.DateField()
    check_time = models.IntegerField(choices=TIME_CHOICES, default=0)
    extra_service = models.IntegerField(choices=SERVICE_CHOICES, default=0)
    
   
    def __str__(self):
        return self.car_reg_number


class Review(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField()
    review_date = models.DateField(auto_now_add=True)



    def __str__(self):
        return f"Review {self.review} by {self.name}"
