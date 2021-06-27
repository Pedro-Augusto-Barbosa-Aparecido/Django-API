from django.urls import path
from salesman.views import SalesmanListView, SalesmanCreateView, SalesmanDeleteView, SalesmanDetailView, SellListView, \
    SellCreateView, SellDetailView


urlpatterns = [
    path("salesman/", SalesmanListView.as_view(), name="list-salesman"),
    path("salesman/create/", SalesmanCreateView.as_view(), name="create-salesman"),
    path("salesman/detail/<int:pk>", SalesmanDetailView.as_view(), name="detail-salesman"),
    path("salesman/delete/<int:pk>", SalesmanDeleteView.as_view(), name="delete-salesman"),
    path("sell/", SellListView.as_view(), name="list-sell"),
    path("sell/create/", SellCreateView.as_view(), name="create-sell"),
    path("sell/detail/<int:pk>", SellDetailView.as_view(), name="detail-sell"),
]