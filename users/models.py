from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    password = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f"{self.pk})  {self.first_name } {self.last_name}"
