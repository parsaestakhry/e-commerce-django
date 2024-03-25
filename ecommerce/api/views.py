from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
# Create your views here.

def hello(request):
    return HttpResponse("hello")


@api_view(['GET'])
def getCustomer(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
