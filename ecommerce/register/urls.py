from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.registerUser, name='user-register')
]
