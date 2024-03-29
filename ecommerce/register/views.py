from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
# Create your views here.
@api_view(['POST'])
def registerUser(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # print(serializer.data)
        userdata = serializer.data
        id = userdata['id']
        user = User.objects.get(id=id)
        # print(user)
        user_group = Group.objects.get(name="customers")
        user.groups.add(user_group)
        # print(user)
        # //print(username)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def authenticateUser(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        return HttpResponse("hello")
    return HttpResponse("no")