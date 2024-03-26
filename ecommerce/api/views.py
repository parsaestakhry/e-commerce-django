from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .models import Customer,Category,Product,Purchase,Manager
from .serializers import CustomerSerializer,CategorySerializer,ProductSerializer,PurchaseSerializer,ManagerSerializer
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
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPurchases(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getManagers(request):
    managers = Manager.objects.all()
    serializer = ManagerSerializer(managers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleCustomer(requues,id):
    customer = Customer.objects.get(id=id)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleCateogory(requues,id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleProduct(requues,id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSinglePurchase(requues,id):
    purchase = Purchase.objects.get(id=id)
    serializer = PurchaseSerializer(purchase, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleManager(requues,id):
    manager = Manager.objects.get(id=id)
    serializer = ManagerSerializer(manager, many=False)
    return Response(serializer.data)







