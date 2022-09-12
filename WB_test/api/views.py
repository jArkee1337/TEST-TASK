from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import *
# Create your views here.

class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]


