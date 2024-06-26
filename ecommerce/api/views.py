from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer,Category,Product,Purchase,Manager,purhase_product_user
from .serializers import CustomerSerializer,CategorySerializer,ProductSerializer,PurchaseSerializer,ManagerSerializer,UserSerializer,Purchase_prouct_user_serializer
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
from django.contrib.auth.models import User
import datetime

# Create your views here.


def hello(request):
    return HttpResponse("helloooo")

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

from django.contrib.auth.models import Group


# @api_view(['POST'])
# def registerUser(request):
#     data = request.data
#     serializer = UserSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         # print(serializer.data)
#         userdata = serializer.data
#         id = userdata['id']
#         user = User.objects.get(id=id)
#         # print(user)
#         user_group = Group.objects.get(name="customers")
#         user.groups.add(user_group)
#         # print(user)
#         # //print(username)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
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


    

@api_view(['GET','POST'])
def get_user_products(request):
    
    data = request.data
    request_token = data['token']
    
    user = Token.objects.get(key=request_token).user
    user_id = user.pk
    
    purchase = Purchase.objects.get(customer=user_id)

    cart_array = purhase_product_user.objects.filter(purchase_id=purchase.pk)
    
    cart_array_serializer = Purchase_prouct_user_serializer(cart_array, many=True)
    
    if cart_array_serializer.is_valid:
        return Response(cart_array_serializer.data)
    
    
    
    return Response("hello")



@api_view(['POST'])
def add_to_user_purchase(request,product_id):
    
    # get user token in request
    data = request.data
    request_token = data['token']
    p_id = int(product_id)
    # get user id using token
    user = Token.objects.get(key=request_token).user
    serializer = UserSerializer(user, many=False)
    username = serializer.data.get('username')
    user_object = User.objects.get(username=username)
    user_id = user_object.pk
    
    # get user purchase using user id
    purchases = Purchase.objects.get(customer=user_id)
    
    purchase_serializer = PurchaseSerializer(purchases, many=False)
    array = purchase_serializer.data
    # print(array)
    # print(username)
    
    
        
    product =  Product.objects.get(id=p_id)
    print(product)
    product.purchase.add(purchases)
           
                 
    return Response("hello")





@api_view(['DELETE'])
def delete_from_list(request,id):
    try:
        # Get user token from request
        # data = request.data
        # request_token = data['token']
        # product_id = int(product_id)
        # product = Product.objects.get(id=product_id)
        # Get user using token
        # user = Token.objects.get(key=request_token).user
        
        # Get user's purchases
        # purchases = Purchase.objects.filter(id=purchase_id)
        
        # Loop through user's purchases
        delete_item = purhase_product_user.objects.get(id=id)
            # Delete from purchase_product_model where product_id and purchase_id match
        purhase_product_user.objects.get(id=id).delete()
        
        return Response("Deletion successful", status=status.HTTP_204_NO_CONTENT)
    
    except Token.DoesNotExist:
        return Response("Invalid token", status=status.HTTP_400_BAD_REQUEST)
    
    except Purchase.DoesNotExist:
        return Response("No purchase found for this user", status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
def add_multiple_to_list(request,product_id,amount):
    # assigning data to a variable
    data = request.data
    # catching the token inside the request
    token = data['token']
    # converting type
    product_id = int(product_id)
    amount = int(amount)
    # accessing the product object
    product = Product.objects.get(id=product_id)
    product_pk = product.pk
    # accessing the user object
    user = Token.objects.get(key=token).user
    user_id = user.pk
    # accessing the purchase object
    purchase = Purchase.objects.get(customer=user_id)
    purchase_amount = product.price * amount
    purhase_product_user.objects.create(
        purchase_id = purchase,
        product_id = product,
        product_amount = amount,
        purchase_amount = purchase_amount
        
    )
    
    print(purhase_product_user.objects.all())
    
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def calculate_cart(request):
     # assigning data to a variable
    # print(request.data)
    data = request.data
    # catching the token inside the request
    token = data['token']
    # converting type
    user = Token.objects.get(key=token).user
    user_id = user.pk
    purchase = Purchase.objects.get(customer=user_id)
    purchase_id = purchase.pk
    cart_array = purhase_product_user.objects.filter(purchase_id=purchase_id)
    
    product_count = 0
    purchase_amount = 0
    
    for item in cart_array:
        purchase_amount = purchase_amount + item.purchase_amount
        product_count = product_count + item.product_amount
        
        
    # print(purchase_amount)
    # print(product_count)
        
    
    return Response({"purchase_amount" : purchase_amount, "product_count" : product_count})