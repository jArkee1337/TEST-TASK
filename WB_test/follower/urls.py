from django.urls import path, include
from api.views import *
from .views import *


urlpatterns = [
    path('', ListFollowerView.as_view()),
    path('<int:pk>', FollowerView.as_view()),


]