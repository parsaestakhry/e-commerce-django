from rest_framework.serializers import ModelSerializer
from .models import Customer,Category,Manager,Product,Purchase

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
    class Meta:
        model = Product
        fields = "__all__"
        

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"
        
        
        

    
    

    