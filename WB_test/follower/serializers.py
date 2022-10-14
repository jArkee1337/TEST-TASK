from rest_framework import serializers
# from api.serializers import UserSerializerForFollower
from .models import Follower
from django.contrib.auth.models import User


class UserOpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class ListByFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserOpSerializer()

    class Meta:
        model = Follower
        fields = ('subscriber',)


class ListFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['user', 'subscriber']
