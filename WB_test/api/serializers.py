from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'posts']

