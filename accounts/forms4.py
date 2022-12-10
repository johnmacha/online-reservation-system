from django.forms import ModelForm
from .models import Registration
from django import forms

class RegistrationViewForm(ModelForm):
    class Meta:
          model = Registration 
          fields = '__all__'

          #__all__