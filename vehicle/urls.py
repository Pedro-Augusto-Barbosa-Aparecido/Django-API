from django.urls import path

from vehicle.views import (
    ProductCreateView,
    ProductDetailView,
    ProductDeleteView,
    ProductListView,
    ProductUpdateView
)

urlpatterns = [
    path('product/', ProductListView.as_view(), name='list-product'),
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
    path('detail-product/<int:pk>', ProductDetailView.as_view(), name='detail-product'),
    path('delete-product/<int:pk>', ProductDeleteView.as_view(), name='detail-product'),
    path('update-product/<int:pk>', ProductUpdateView.as_view(), name='update-product'),
]
