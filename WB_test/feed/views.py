from rest_framework import permissions, generics
from rest_framework.pagination import PageNumberPagination

from api.models import Post
from api.serializers import PostSerializer

class FeedListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class FeedView(generics.ListAPIView):
    """ View follower`s feed
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = FeedListPagination

    def get_queryset(self):


        qs = Post.objects.filter(author__owner__subscriber=self.request.user).order_by('-created_at').select_related('author')
        return qs



