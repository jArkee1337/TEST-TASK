from django.urls import path, include
from api.views import *
from .views import UserProfileListView


urlpatterns = [
    path('', PostAPIList.as_view()),
    path("all-profiles/",UserProfileListView.as_view()),
    path("other-posts/",PostOtherUsersAPIList.as_view()),

]