from email.policy import default
from socket import fromshare
from django import forms
from django.core import validators
#from django.core.validators import MinValueValidator, MaxValueValidator

#from views import validate_current_year


class AvailabilityForm(forms.Form):
    
    check_in = forms.DateTimeField(required=True, input_formats = ["%Y-%m-%dT%H:%M"])
    check_out = forms.DateTimeField(required=True, input_formats = ["%Y-%m-%dT%H:%M"])
