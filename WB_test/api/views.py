from django.shortcuts import render
from requests import Response

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import *
from django.db.models import Count

# Create your views here.

class CreatePostAPIView(generics.CreateAPIView):
    """
    Create new post, only for authenticated users
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostOtherUsersAPIList(generics.ListAPIView):
    """
    The list of posts that other users created
    """
    def get_queryset(self):
        qs = Post.objects.all().exclude(author=self.request.user.id).order_by('created_at')
        return qs

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]


class UserProfileListView(generics.ListAPIView):
    """
    The list of all users
    """
    queryset = User.objects.all().annotate(cnt=Count('posts')).order_by('-cnt', '-pk')
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]





