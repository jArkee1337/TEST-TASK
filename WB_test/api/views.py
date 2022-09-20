from django.shortcuts import render
from requests import Response

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import *
from django.db.models import Count

# Create your views here.

class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]

class PostOtherUsersAPIList(generics.ListCreateAPIView):
    def get_queryset(self):
        qs = Post.objects.all().exclude(author=self.request.user.id).order_by('created_at')
        return qs

    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]


class UserProfileListView(generics.ListAPIView):
    queryset = User.objects.all().annotate(cnt=Count('author')).order_by('-cnt')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]





