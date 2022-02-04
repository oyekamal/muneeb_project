from termios import VSWTCH
from rest_framework import viewsets
from .models import Vehicle, DailyVehicleUpdate
from .serializer import VehicleSeralizer
from rest_framework.response import Response
from datetime import datetime


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSeralizer

    def partial_update(self, request, *args, **kwargs):
        id_ = kwargs.get('pk')
        vehicle = Vehicle.objects.filter(id=id_).first()
        if vehicle:
            today_mileage = int(request.data['mileage']) - int(vehicle.mileage)

            print("today_mileage ----> ", today_mileage)

            if today_mileage >= 0:

                DailyVehicleUpdate.objects.create(
                    vehicle=vehicle, mileage=today_mileage).save()

        return super().partial_update(request, *args, **kwargs)

    def mileage_details(self, request):

        date = self.request.query_params.get('date')
        regisration_number = self.request.query_params.get(
            'regisration_number')

        if date and regisration_number:

            date_time_obj = datetime.strptime(date, '%d/%m/%y')

            data = DailyVehicleUpdate.objects.filter(
                date__gte=date_time_obj, vehicle__regisration_number=regisration_number).values()

            mileages = 0
            for each_data in data:
                mileages += each_data["mileage"]

            return Response({"from_date": date, "regisration_number": regisration_number,
                             "total_mileages": mileages})
        return Response({})
