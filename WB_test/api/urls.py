from django.urls import path, include
from api.views import *
from .views import UserProfileListView


urlpatterns = [
    path('post/', CreatePostAPIView.as_view(), name='create_post'),
    path("all-users/",UserProfileListView.as_view(), name='profiles'),
    path("other-users-posts/",PostOtherUsersAPIList.as_view(), name='other-users-posts'),

]