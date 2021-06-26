from django.urls import path

from vehicle.views import ProductCreateView

urlpatterns = [
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
]
