from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
