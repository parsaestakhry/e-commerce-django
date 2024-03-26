from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer,Category,Product,Purchase,Manager
from .serializers import CustomerSerializer,CategorySerializer
from rest_framework.response import Response
# Create your views here.

def hello(request):
    return HttpResponse("hello")


@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CustomerSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = CustomerSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPurchases(request):
    purchases = Purchase.objects.all()
    serializer = CustomerSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getManagers(request):
    managers = Manager.objects.all()
    serializer = CustomerSerializer(managers, many=True)
    return Response(serializer.data)







