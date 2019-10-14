from django.contrib import admin
from . models import Vehicle, Owner, VehicleEntry, Person

admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Owner)
admin.site.register(VehicleEntry)
