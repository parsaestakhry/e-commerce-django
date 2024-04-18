from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer,Category,Product,Purchase,Manager
from .serializers import CustomerSerializer,CategorySerializer,ProductSerializer,PurchaseSerializer,ManagerSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
import datetime

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


@api_view(['GET'])
def getCategoryProducts(request):
    products = Product.objects.filter(category_id=2).values()
    print(products)
    # serializer = ProductSerializer(products, many=True)
    # print(serializer.data)
    # print(products)
    
    return HttpResponse("hello")
    
    
    
class productList(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        params = self.request.query_params.get('category')
        if params is not None:
            queryset = queryset.filter(category_id=params)
        
        # print(queryset)
            
        return queryset

@api_view(['GET'])
def getCategoryIdProducts(request, category):
    category = Category.objects.get(name=category)
    serializer = CategorySerializer(category, many=False)
    data = serializer.data
    category_id = data['id']
    print(category_id)
    products = Product.objects.filter(category=category_id)
    print(products)
    productsSerilizer = ProductSerializer(products, many=True)
    
    return Response(productsSerilizer.data)




    
    
    
class authenticate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth' : str(request.auth),
        }
        return Response(content)
    
    
    
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    
    
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

from datetime import datetime, timedelta

from datetime import datetime, timedelta
from django.utils import timezone

@api_view(['POST'])
def UserLoginView(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username or password is missing'}, status=400)

        user = authenticate(username=username, password=password)
        
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            response = JsonResponse({'message': 'Login successful','token':token.key})
            
            # Set cookie to expire in 30 days
            expiry_date = timezone.now() + timedelta(days=30)
            
            response.set_cookie(
                'auth_token', 
                token.key, 
                httponly=False, 
                expires=expiry_date,
                samesite=None
            )  # Setting token as a cookie
            
            return response
            
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


    

@api_view(['GET'])
def get_user_products(request):
    
    cookie = request.COOKIES['auth_token']
    
    return Response(cookie)


        

    













    
    
    
    
        


