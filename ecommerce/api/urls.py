from . import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name="hello"),
    path("get-customers/", views.getCustomers, name="get-customers"),
    path("get-categories/", views.getCategories, name="get-categories"),
    path("get-managers/", views.getManagers, name="get-managers"),
    path("get-products/", views.getProducts, name="get-products"),
    path("get-purchases/", views.getPurchases, name="get-purchases"),
    path("get-customer/<int:id>/", views.getSingleCustomer, name='get-customer'),
    path("get-category/<int:id>/", views.getSingleCateogory, name='get-category'),
    path("get-product/<int:id>/", views.getSingleProduct, name='get-product'),
    path("get-purchase/<int:id>/", views.getSinglePurchase, name='get-purchase'),
    path("get-manager/<int:id>/", views.getSingleManager, name='get-manager'),
    
]
