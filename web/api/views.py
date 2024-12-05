
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from web_app.models import (
    User, Game, UserModel
)
from api.serializers import (
    GameSerializer, UserModelSerializer
)
from rest_framework import generics
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import login as django_login, logout as django_logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.views import APIView
from datetime import datetime, timedelta
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
import sys
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404

# Start Controller Game
class GameListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer

class GameDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer

class GameSearch(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GameSerializer

    def get_queryset(self, *args, **kwargs):
        query_list = Game.objects.all()        
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(
                Q(name__icontains = query)                
    	    ).distinct()
            return query_list
# End Controller Game

# Start Controller Game
class UserModelListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = UserModel.objects.all().order_by('id')
    serializer_class = UserModelSerializer

class UserModelDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = UserModel.objects.all().order_by('id')
    serializer_class = UserModelSerializer

class UserModelSearch(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        query_list = UserModel.objects.all()        
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(
                Q(name__icontains = query)                
    	    ).distinct()
            return query_list
# End Controller UserModel

# # Start Controller MenuResto
# class MenuRestoFilterApi(generics.ListAPIView):
#     queryset = MenuResto.objects.all()
#     serializer_class = MenuRestoSerializer    
#     pagination_class = CustomPagination
#     permission_classes = [permissions.IsAuthenticated]
#     # permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['category__name', ]
#     ordering_fields = ['created_on']

# class MenuRestoSearchApi(generics.ListAPIView):
#     serializer_class = MenuRestoSerializer
#     permission_classes = [IsAuthenticated]



# class MenuRestoFilterApi(generics.ListAPIView):
#     queryset = MenuResto.objects.all()
#     serializer_class = MenuRestoSerializer
#     # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     # filterset_fields = ['category__name', ]
#     # ordering_fields = ['created_on']
#     # pagination_class = CustomPagination
#     # permission_classes = [permissions.IsAuthenticated]

