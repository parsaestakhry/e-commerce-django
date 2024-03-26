from . import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name="hello"),
    # get multiple items
    path("get-customers/", views.getCustomers, name="get-customers"),
    path("get-categories/", views.getCategories, name="get-categories"),
    path("get-managers/", views.getManagers, name="get-managers"),
    path("get-products/", views.getProducts, name="get-products"),
    path("get-purchases/", views.getPurchases, name="get-purchases"),
    
    # get single item
    path("get-customer/<int:id>/", views.getSingleCustomer, name='get-customer'),
    path("get-category/<int:id>/", views.getSingleCateogory, name='get-category'),
    path("get-product/<int:id>/", views.getSingleProduct, name='get-product'),
    path("get-purchase/<int:id>/", views.getSinglePurchase, name='get-purchase'),
    path("get-manager/<int:id>/", views.getSingleManager, name='get-manager'),
    
    # create single item
    path('create-customer/', views.createCustomer, name='create-customer'),
    path('create-category/', views.createCategory, name='create-category'),
    path('create-product/', views.createProduct, name='create-product'),
    path('create-purchase/', views.createPurchase, name='create-purchase'),
    path('create-manager/', views.createManager, name='create-manager'),
    
    # update single item 
    path('update-customer/<int:id>/', views.updateCustomer, name='update-customer'),
    path('update-category/<int:id>/', views.updateCategory, name='update-category'),
    path('update-manager/<int:id>/', views.updateManager, name='update-manager'),
    path('update-product/<int:id>/', views.updateProduct, name='update-product'),
    path('update-purchase/<int:id>/', views.updatePurchase, name='update-purchase'),
    
    
    
]
