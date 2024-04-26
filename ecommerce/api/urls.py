from . import views
from django.urls import path
from django.urls import re_path

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
    
    # delete single item
    path('delete-customer/<int:id>/', views.deleteCustomer, name='delete-customer'),
    path('delete-category/<int:id>/', views.deleteCategory, name='delete-category'),
    path('delete-purchase/<int:id>/', views.deletePurchase, name='delete-purchase'),
    path('delete-product/<int:id>/', views.deleteProduct, name='delete-product'),
    path('delete-manager/<int:id>/', views.deleteManager, name='delete-manager'),
    
    
    # get products in category
    # re_path(r'^api/products/category/(?P<category>\w+)/$', productCategoryList.as_view() , name='get_category_product'),
    # path('get-category-products/', views.getCategoryProducts, name='get-category-products'),
    path('get-category-products/', views.productList.as_view(), name='hello'),
    path('get-category-id/<str:category>/' , views.getCategoryIdProducts, name='get-category'),
    # path('authenticate/', views.authenticate.as_view(), name='authenticate'),
    
    # register views
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path("login/", views.UserLoginView, name="user-login"),
    # user list
    path('get-user-list/', views.get_user_products, name='get-user-list'),
    path('add-to-list/<int:product_id>/', views.add_to_user_purchase, name='add-to-user-list'),
    path('remove-from-list/<int:id>/', views.delete_from_list, name='remove-from-list'),
    path('add-multiple-list/<int:product_id>/<int:amount>/', views.add_multiple_to_list, name='add-multiple-to-list')
    
    
    
    
]
