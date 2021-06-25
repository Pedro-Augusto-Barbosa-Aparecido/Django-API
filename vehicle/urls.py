from django.urls import path

from vehicle.views import VehicleCreateView

urlpatterns = [
    path('create/', VehicleCreateView.as_view(), name='create-vehicle')
]
