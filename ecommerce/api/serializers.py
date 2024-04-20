from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customer,Category,Manager,Product,Purchase
from django.contrib.auth.models import User

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        
        

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"
        
        

class ProductSerializer(ModelSerializer):
    category= serializers.SlugRelatedField(
        slug_field='name',
        queryset = Category.objects.all()
    )
    class Meta:
        model = Product
        fields = "__all__"
        

class PurchaseSerializer(ModelSerializer):
    customer = serializers.SlugRelatedField(
        slug_field='username',
        queryset = User.objects.all()
    )
    class Meta:
        model = Purchase
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
        

        
        

    
    

    