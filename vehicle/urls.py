from django.urls import path

from vehicle.views import VehicleCreateView, ProductCreateView

urlpatterns = [
    path('create-vehicle/', VehicleCreateView.as_view(), name='create-vehicle'),
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
]
