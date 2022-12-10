from django.contrib import admin
from .models import Availability, Destination, Room, Booking


# Register your models here.
admin.site.register(Destination)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Availability)
#admin.site.register(MpesaPayment)


