from email.policy import default
from django.db import models
from datetime import datetime, date

# Create your models here.
class Registration(models.Model):
     first_name = models.CharField(max_length = 20)
     second_name  = models.CharField(max_length = 20)
     last_name = models.CharField(max_length = 20)
     tel_number = models.IntegerField()
     location = models.CharField(max_length = 20)
     postal_code = models.IntegerField()
     id_number = models.IntegerField()
     GENDER=[
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER'),
     ]
     gender = models.CharField(max_length = 6, choices = GENDER, default = None)
     date_of_birth = models.DateField(max_length = 8)
     date_of_register = models.DateField(max_length = 8)
     email = models.EmailField(max_length = 40)

     def __str__(self):
        return f'{self.first_name} {self.second_name} whose phone number is {self.tel_number} from {self.location} and gender {self.gender} registered on {self.date_of_register} with email {self.email}'





    

