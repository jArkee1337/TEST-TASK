from django.shortcuts import render
from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import ListByFollowerSerializer
from django.contrib.auth.models import User


class ListFollowerView(generics.ListAPIView):
    """ The list of user's subscribers
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListByFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class CreateDeleteFollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """
        Add to followers
        """
        try:
            user = User.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        """Delete from followers
        """
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)

        except User.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)
