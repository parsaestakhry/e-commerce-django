from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.registerUser, name='user-register'),
    path('user-login/', views.authenticateUser, name='user-authentication')
]
