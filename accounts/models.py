# Accounts/ Models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.

class User(AbstractUser):
    # Links UserProfile to a User model instance.
    mobile = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=25, blank=True)
    userbio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    doj = models.DateTimeField(editable=False, auto_now_add=True, null=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.username
