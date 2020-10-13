from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
