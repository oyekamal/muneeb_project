from rest_framework import routers
from django.urls import path, include
from .views import VehicleViewSet


router = routers.DefaultRouter()
router.register(r'vehicle', VehicleViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('mileage_details', VehicleViewSet.as_view({'get': 'mileage_details'})),

]

