from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    feedback = models.TextField()

class RestaurantReservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    date = models.DateField()
    guests = models.IntegerField()
    additionally = models.TextField()
    
class ConferenceHallReservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    date = models.DateField()
    guests = models.IntegerField()
    additionally = models.TextField()

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    adults_amount = models.IntegerField()
    children_amount = models.IntegerField()
    room_type = models.CharField(max_length=100)
    comment = models.TextField(blank=True)