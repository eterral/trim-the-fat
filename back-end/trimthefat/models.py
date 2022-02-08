from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Subscription(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField(max_length=128)
    cost = models.CharField(max_length=128)
    unsubscribe = models.URLField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
	    return self.title
