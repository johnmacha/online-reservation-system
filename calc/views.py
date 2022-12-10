#from unicodedata import name
from . import views
from unicodedata import category
from django.shortcuts import HttpResponse,render, redirect
from django.http import FileResponse
import io 
import datetime
from io import BytesIO
#from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
#from .filters import ListingFilter
from django.template.loader import get_template
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Destination, Room, Booking, Availability
from mpesa.models import MpesaPay
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms1 import DestinationForm
from .forms3 import RoomForm
from .forms import AvailabilityForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from .forms import AvailabilityForm
from calc.booking_functions.availability import check_availability
from .decorators import unauthenticated_user, allowed_users

from calc import forms3

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin'])
def admins(request):
    if request.method == 'POST':
       print(request.POST)
       username = request.POST.get('username')
       password = request.POST.get('password')


       user = auth.authenticate(request, username = username, password = password)
       if user is not None:
        auth.login(request, user)
        return redirect("/room_add/")
       else:
         messages.info(request,"invalid credentials")
         return redirect('admins')
    
    else:  
     #request.user.is_authenticated:
     #   return redirect('admins')
       return render(request,'admin.html')

def report1(request):
    pay = MpesaPay.objects.all()

    template_path = ''
    context = {'pay':pay}
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-DIsposition'] = "filename = payment.pdf"
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest = response)
    
    if pisa_status.err:
        return HttpResponse('we had some errors<pre>'+ html + '</pre>' ) 
    return response     

def reports(request):
    title = 'Customers report'
    query=MpesaPay.objects.all()
    context={
        "title":title,
        "query":query
    }
    return render(request, 'report.html',context) 


def list(request):
    title = 'Booking List'
    list=Booking.objects.all()
    context={
        "title":title,
        "list":list
    }
    return render(request, 'final_list.html',context)

def selection(request):
    return render(request, 'test1.html')

def validate_current_year(value):
    if value < 2022  or value > 2050:
        raise ValidationError(u'%s is not a valid year!' % value)

@login_required(login_url='/accounts/login')
def add(request):
    form = DestinationForm()
    if request.method == 'POST':
        #print(request.POST)
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()

    context = {'form':form}
    return render(request,'room_add.html', context)

@login_required(login_url='/accounts/login')
def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login')
def home(request):
      dests = Destination.objects.all()

      return render(request, 'store.html',{'dests':dests}) 

@login_required(login_url='/accounts/login')
def RoomListView(request):
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
    print('categories=', room_categories)
   
    room_values = room_categories.values()
    print('categories=',room_values)
    room_list = []
    context={}

    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('calc:RoomDetailView', kwargs ={'category':room_category} )
        room_list.append((room, room_url))   
        context = {
            "room_list":room_list,
        }

    return render(request,'store.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def select(request):
    forms3 = RoomForm()
    if request.method == 'POST':
        #print(request.POST)
        forms3 = RoomForm(request.POST)
        if forms3.is_valid():
            forms3.save()
    context = {'forms3':forms3}
    return render(request,'room_select.html',context)

class BookingList(ListView):
    model = Booking
    template_name = "booking_list.html"

    def get_context_data(self, **kwargs):
         
        return super().get_context_data(
            booking = self.request.user.booking_set.all(),
            **kwargs)
  #return render(request,'login.html')

def AvailabilityList(request):
    title = 'Available Rooms'
    all = Room.objects.all()
    context = {
        "title":title,
        "all": all
    }
    return render(request,'room_available.html',context)

class RoomDetailView(View):
    # **kwargs allows us to pass a variable number of keyword arguments to a python function
    # *args allows us to pass a variable number of non-keyword arguments to a python function

  #@login_required(login_url='/accounts/registration')
  def get(self, request,*args, **kwargs):
      category = self.kwargs.get('category', None)
      form = AvailabilityForm()
      room_list = Room.objects.filter(category = category)
      if len(room_list)>0:
          room = room_list[0]
          room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
          context={
               'room_category':room_category,
               'form':form,
          }
          return render(request,'room_detail.html',context)
      else:
          return HttpResponse('Category does not exist')

# def clean_date(self):
#     date = self.cleaned_data['date']
#     if date < datetime.date.today():
#         raise ValidationError(self.error_messages['Date cannot be in the past'], code='Date cannot be in the past')
#     return date



  def post(self, request,*args, **kwargs):
     category = self.kwargs.get('category', None)
     room_list = Room.objects.filter(category = category)
     form = AvailabilityForm(request.POST)
    
     if form.is_valid():
        data = form.cleaned_data

     available_rooms=[]
     for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
              available_rooms.append(room)

     if len(available_rooms) > 0:       
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            booking.save()
            return  HttpResponse(booking)

        #Check here
     else:
          return HttpResponse('All of this category of rooms are booked! Try another one.')



#This is a generic model
class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('calc:BookingList')


#--------------MPESA-------------------------------
