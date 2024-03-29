from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer,Category,Product,Purchase,Manager
from .serializers import CustomerSerializer,CategorySerializer,ProductSerializer,PurchaseSerializer,ManagerSerializer
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def hello(request):
    return HttpResponse("hello")

# get multiple items

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

# get single item

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


# create model objects 


@api_view(['POST'])
def createCustomer(request):
    if request.method == "POST":
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def createCategory(request):
    if request.method == "POST":
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createProduct(request):
    if request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def createPurchase(request):
    if request.method == "POST":
        data = request.data
        serializer = PurchaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def createManager(request):
    if request.method == "POST":
        data = request.data
        serializer = ManagerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    

#update item


@api_view(['PUT'])
def updateCustomer(request,id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = CustomerSerializer(instance=customer,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT'])
def updateCategory(request,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = CategorySerializer(instance=category,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def updateProduct(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def updatePurchase(request,id):
    try:
        purchase = Purchase.objects.get(id=id)
    except Purchase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = PurchaseSerializer(instance=purchase,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def updateManager(request,id):
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = ManagerSerializer(instance=manager,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# delete single item


@api_view(['DELETE'])
def deleteCustomer(request,id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    customer.delete()
    return HttpResponse("deleted")


@api_view(['DELETE'])
def deleteCategory(request,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return HttpResponse("deleted")


@api_view(['DELETE'])
def deleteProduct(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return HttpResponse("deleted")


@api_view(['DELETE'])
def deletePurchase(request,id):
    try:
        purchase = Purchase.objects.get(id=id)
    except Purchase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    purchase.delete()
    return HttpResponse("deleted")


@api_view(['DELETE'])
def deleteManager(request,id):
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    manager.delete()
    return HttpResponse("deleted")



def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)









    
    
    
    
        


