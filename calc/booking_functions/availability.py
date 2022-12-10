import datetime
from django.shortcuts import render, redirect
from calc.models import Room, Booking, Availability

def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
           avail_list.append(True)
        else:
           avail_list.append(False)
        #'any' returns TRUE in any FALSE in the list and FALSE if everything is TRUE
        #'all' returns TRUE in all TRUE but False in any FALSE
    return all(avail_list)

