from django.urls import path, include
from api.views import PostAPIList
from .views import UserProfileListCreateView, userProfileDetailView


urlpatterns = [
    path('', PostAPIList.as_view()),
#gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),


]