from django.urls import path, include
from api.views import *
from .views import *


urlpatterns = [
    path('', ListFollowerView.as_view(), name='followers'),

    path('<int:pk>', CreateDeleteFollowerView.as_view(), name='change_follower'),


]