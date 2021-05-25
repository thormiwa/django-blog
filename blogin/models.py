from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    username = models.CharField(blank=True, null=True, max_length=100)
    REQUIRED_FIELDS = ['name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email