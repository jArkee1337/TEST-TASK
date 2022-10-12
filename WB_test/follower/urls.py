from django.urls import path, include
from api.views import *
from .views import *


urlpatterns = [
    path('', ListCreateFollowerView.as_view()),

    path('<int:pk>', DeleteFollowerView.as_view()),


]