from . import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name="hello"),
    path("get-customers/", views.getCustomers, name="get-customers"),
    path("get-categories/", views.getCategories, name="get-categories"),
    path("get-managers/", views.getManagers, name="get-managers"),
    path("get-products/", views.getProducts, name="get-products"),
    path("get-purchases/", views.getPurchases, name="get-purchases"),
]
