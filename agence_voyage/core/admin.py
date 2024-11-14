from django.contrib import admin
from .models import Destination, Hotel, OffreVoyage, Reservation
# Register your models here.
admin.site.register(Destination)
admin.site.register(Hotel)
admin.site.register(OffreVoyage)
admin.site.register(Reservation)
