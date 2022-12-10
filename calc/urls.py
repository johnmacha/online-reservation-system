from django.urls import path

from calc.models import Availability
from .views import RoomListView, BookingList, RoomDetailView, CancelBookingView, AvailabilityList  
from . import views

app_name = 'calc'   

urlpatterns = [
   
path('',views.welcome, name= 'welcome'),
path('home/',views.home, name='home'),
path('room_select/',views.select,name ='select'),
#path('hotel/', views.hotel, name='hotel'),
path('selection/',views.selection, name='selection'),
path('room_add/', views.add, name='add'),
path('room_available/', views.AvailabilityList, name='AvailabilityList'),
path('booking_list/', BookingList.as_view(), name = 'BookingList'),
path('room/<category>',RoomDetailView.as_view(), name = 'RoomDetailView'),
path('admins/', views.admins, name = 'admins'),
path('reports/', views.reports, name='reports' ),
path('report/', views.report1, name = 'report' ),
path('list/', views.list, name='list'),
path('booking/cancel/<pk>', CancelBookingView.as_view(), name = 'CancelBookingView'),

]