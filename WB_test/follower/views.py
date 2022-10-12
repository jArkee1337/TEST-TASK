from django.shortcuts import render
from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import ListFollowerSerializer
from django.contrib.auth.models import User


class ListCreateFollowerView(generics.ListCreateAPIView):
    """ The list of user's subscribers
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)



class DeleteFollowerView(views.APIView):
    """ Delete from subscribers
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
            print(sub.user_id)

        except User.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)