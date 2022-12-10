from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

#from .models import Registration 

class RegistrationForm(UserCreationForm):
     first_name = forms.CharField(max_length = 20, required = True, help_text = 'Required')
     last_name = forms.CharField(max_length = 20, required = True, help_text = 'Required')
     email = forms.EmailField(required = True)

     class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
     @transaction.atomic
     def save(self, commit = True):
        user = super(RegistrationForm,self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        user.email = self.cleaned_data['email']
        return user