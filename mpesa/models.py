from django.db import models
from django.utils import timezone

#Create your models here.
class MpesaPay(models.Model):
    first_name = models.CharField(max_length = 20)
    second_name = models.CharField(max_length = 20)
    #date_of_payment  = models.DateField(default=timezone.now,null=True)
    phone_number  = models.IntegerField()
    amount = models.IntegerField()