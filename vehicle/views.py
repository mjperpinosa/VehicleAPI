from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Person, Vehicle, Owner, VehicleEntry
from .serializers import VehicleEntrySerializer


class HotListView(APIView):
    def get(self, request):
        data = Vehicles.objects.filter(~Q(status='CLEARED'))
        serializer = VehicleSerializer(data, many=True)

        return Response(serializer.data)

class VehicleEntryHotListView(APIView):
    def get(self, request):
        data = VehicleEntry.objects.filter(~Q(owner__vehicle__status=Vehicle.status_choices.CL))
        serializer = VehicleSerializer(data, many=True)

        return Response(serializer.data)

class VehicleEntryCarnapped(APIView):
    def get(self, request):
        data = VehicleEntry.objects.filter(owner__vehicle__status=Vehicle.status_choices.CA)
        serializer = VehicleSerializer(data, many=True)

        return Response(serializer.data)

class VehicleEntryUnregistered(APIView):
    def get(self, request):
        data = VehicleEntry.objects.filter(owner__vehicle__status=Vehicle.status_choices.UN)
        serializer = VehicleSerializer(data, many=True)

        return Response(serializer.data)

class VehicleEntryDuplicate(APIView):
    def get(self, request):
        data = VehicleEntry.objects.filter(owner__vehicle__status=Vehicle.status_choices.DU)
        serializer = VehicleSerializer(data, many=True)

        return Response(serializer.data)

class VehicleEntryCodingViolation(APIView):
    def get(self, request):
        status = request.data.get('status')

        data = VehicleEntry.objects.filter(owner__vehicle__status=query)
        serializer = VehicleSerializer(data, many=True)

        return Response(serializer.data)

class VehicleEntryView(APIView):
    def get(self, request):
        data = VehicleEntry.objects.all().order_by('-time_entry')
        serializer = VehicleEntrySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        plate_number = request.data.get('plate_number')

        try:
            # vehicle = Vehicle.objects.get(vehicle__plate_number=plate_number)
            owner = Owner.objects.get(vehicle__plate_number=plate_number)

            new_entry = VehicleEntry.objects.create(owner=owner)

        except Owner.DoesNotExist:
            new_entry = None

        serializer = VehicleEntrySerializer(new_entry, many=False)

        return Response(serializer.data)

def get_stats(request):
    total_hot_vehicles = VehicleEntry.objects.filter(~Q(owner__vehicle__status=Vehicle.status_choices.CL)).count()
    total_entry = VehicleEntry.objects.all().count()


    return Response({"total_hot_vehicles": vehicle_entry_count, "total_entry": total_entry})
