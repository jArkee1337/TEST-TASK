from rest_framework import serializers
from api.serializers import UserSerializerForFollower
from .models import Follower

class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserSerializerForFollower(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)