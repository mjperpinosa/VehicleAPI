from rest_framework import serializers
from .models import Vehicle, VehicleEntry, Owner, Person

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=False, read_only=True)
    vehicle = VehicleSerializer(many=False, read_only=True)

    class Meta:
        model = Owner
        fields = '__all__'

class VehicleEntrySerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=False, read_only=True)

    class Meta:
        model = VehicleEntry
        fields = '__all__'
