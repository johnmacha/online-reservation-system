from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core import validators
#from django.core.validators import MinValueValidator, MaxValueValidator
#from views import validate_current_year


# Create your models here.


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('DELU','DELUXEDOUBLE'),
        ('DEL','DELUXEROOM'),
        ('STAN','STANDARDROOM')
        )

    number = models.IntegerField()
    category = models.CharField(max_length = 200,choices = ROOM_CATEGORIES)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} for {self.capacity} people'

class Availability(models.Model):
    ROOM_CATEGORIES = (
        ('DELU','DELUXEDOUBLE'),
        ('DEL','DELUXEROOM'),
        ('STAN','STANDARDROOM')
        )

    category = models.CharField(max_length = 200,choices = ROOM_CATEGORIES)
    number = models.IntegerField()
    capacity = models.IntegerField()

class Destination(models.Model):
    
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='images/')
    desc=models.TextField() 
    price= models.IntegerField()

class Booking(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
     room = models.ForeignKey(Room, on_delete= models.CASCADE)
     check_in = models.DateTimeField()
     check_out = models.DateTimeField()

     def __str__(self):
      return f'From = {self.check_in} To = {self.check_out} '

 # These are generic views
     def get_room_category(self):
       room_categories= dict(self.room.ROOM_CATEGORIES)
       room_category = room_categories.get(self.room.category)
       return room_category
     
     def get_cancel_booking_url(self):
        return reverse('calc:CancelBookingView', args = [self.pk,])
        

#---------------------MPESA----------------------------------
# class MpesaPay(models.Model):
#     first_name = models.CharField(max_length = 20)
#     second_name = models.CharField(max_length = 20)
#    # date_of_payment  = models.DateTimeField(max_length=8)
#     phone_number  = models.IntegerField()
#     amount = models.IntegerField()
