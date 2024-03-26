from . import views
from django.urls import path

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("get-customer/", views.getCustomers, name="get-customers")
]
