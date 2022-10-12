from rest_framework import serializers
# from api.serializers import UserSerializerForFollower
from .models import Follower
from django.contrib.auth.models import User


# class UserByFollowerSerializer(serializers.ModelSerializer):
#     subscribers = serializers.PrimaryKeyRelatedField(many=True, queryset=Follower.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'subscribers',)
class ListFollowerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Follower
        fields = ['user', 'subscriber']



