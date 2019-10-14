from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=64, unique=True)
    engine_number = models.CharField(max_length=64)
    chassis_number = models.CharField(max_length=64)
    vehicle_type = models.CharField(max_length=64)
    number_of_cylinders = models.CharField(max_length=64)
    gross_weight = models.CharField(max_length=64)
    body_type = models.CharField(max_length=64)
    fuel_type = models.CharField(max_length=64)
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    year = models.CharField(max_length=64)
    color = models.CharField(max_length=64, default='white')

    CL = 'CLEARED'
    UN = 'UNREGISTERED'
    CA = 'CARNAPPED'
    DU = 'DUPLICATE'
    CO = 'CODING'
    status_choices = [
        (CL, 'Cleared'),
        (UN, 'Unregistered'),
        (CA, 'Carnapped'),
        (DU, 'Duplicate'),
        (CO, 'Coding Violation')
    ]

    status = models.CharField(max_length=64, choices=status_choices, default=CL)


    def __str__(self):
        return self.plate_number

class Owner(models.Model):
    or_number = models.CharField(max_length=64, unique=True)
    date = models.CharField(max_length=64)
    registration_office = models.CharField(max_length=64)
    certificate_number = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.person.first_name, self.person.last_name)

class VehicleEntry(models.Model):
    time_entry = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
