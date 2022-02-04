from atexit import register
from django.db import models
from django.db.models.signals import post_save


# Create your models here.
class Vehicle(models.Model):
    mileage = models.BigIntegerField()
    manufacturer = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    regisration_number = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return self.regisration_number + ' : ' + self.manufacturer


class DailyVehicleUpdate(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    mileage = models.BigIntegerField()

    def __str__(self) -> str:
        return self.vehicle.regisration_number + " : " + str(self.date)

    class Meta:
        ordering = ('-date',)


def save_profile(sender, instance, **kwargs):

    if not Vehicle.objects.filter(regisration_number=instance.regisration_number).exists():
        print("yooooo yeeeaaaaahhhhhh ")
        DailyVehicleUpdate.objects.create(vehicle=instance, mileage=0).save()


post_save.connect(save_profile, sender=Vehicle)
