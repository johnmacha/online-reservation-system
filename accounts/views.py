from multiprocessing import context
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .forms2 import RegistrationForm
from .forms4 import RegistrationViewForm
from .models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users

from accounts import forms4

# Create your views here.
def loginPage(request):
     if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')


       user = auth.authenticate(request, username = username, password = password)
       if user is not None:
        auth.login(request, user)
        return redirect("/")
       else:
         messages.info(request,"invalid credentials")
         return redirect('login')
    
     else:  
      return render(request,'login.html')
 
def registerPage(request):
 
    form1 = RegistrationForm()
    if request.method == 'POST':
      # print(request.POST)
        form1 = RegistrationForm(request.POST)
        if form1.is_valid():
             form1.save()
             user = form1.cleaned_data.get('username')
             messages.success(request, 'Your account has been created successfully for '+ user)   
            
             return redirect('login')
    return render(request,'register.html',context = {'form1':form1})

      #username = request.POST['username']
      #email = request.POST['email']
      #subject = 'Welcome to Sportsview hotel'
      #message = f'Hi {username} enjoy the services on offer. Good luck.'
      #from_email = settings.EMAIL_HOST_USER 
      #recipient_list = [email]
     # send_mail(subject, message, from_email,recipient_list, fail_silently=False)
      # 
       #
       #
  #else:
     # form1 = RegistrationForm()

      #messages.info(redirect,"Details already taken")

def registration(request):
   
   # book = Registration.objects.get(id=uid)
    form2 = RegistrationViewForm()
    if request.method == 'POST':
     # print(request.POST)
      booking = Registration.objects.create(
        first_name = request.POST.get('first_name'),
        second_name = request.POST.get('second_name'),
        last_name = request.POST.get('last_name'),
        tel_number = request.POST.get('tel_number'),
        location = request.POST.get('location'),
        postal_code = request.POST.get('postal_code'),
        id_number = request.POST.get('id_number'),
        gender = request.POST.get('gender'),
        date_of_birth = request.POST.get('date_of_birth'),
        date_of_register = request.POST.get('date_of_register'),
        email = request.POST.get('email')
      )
      form2 = RegistrationViewForm(request.POST)
      if form2.is_valid():
         form2.save()
         return render(request,'mpesa.html')
   
    return render(request, 'register_view.html',context = {'forms4':forms4}) 
 
def logout(request):
  auth.logout(request)
  return redirect("/")

def about(request):
  return render(request,'about.html')

@login_required
@allowed_users(allowed_roles=['admin'])
def admin(request):
  if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')

     user = auth.authenticate(request, username = username, password = password)
     if user is not None:
        auth.login(request, user)
        return render(request,'admin_page.html')
     else:
         messages.info(request,"invalid credentials")
         return redirect('admin')
    
  else:  
    return render(request,'admin.html')

    
 
 