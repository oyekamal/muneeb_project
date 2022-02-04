from rest_framework import serializers
from .models import Vehicle, DailyVehicleUpdate

class VehicleSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'