from termios import VSWTCH
from rest_framework import viewsets
from .models import Vehicle, DailyVehicleUpdate
from .serializer import VehicleSeralizer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSeralizer

    def partial_update(self, request, *args, **kwargs):
        id_ = kwargs.get('pk')
        vehicle = Vehicle.objects.filter(id = id_).first()
        if vehicle:
            today_mileage = int(request.data['mileage']) - int(vehicle.mileage) 

            print("today_mileage ----> ",today_mileage)

            if today_mileage >= 0:

                DailyVehicleUpdate.objects.create(vehicle=vehicle, mileage = today_mileage).save()

        return super().partial_update(request, *args, **kwargs)