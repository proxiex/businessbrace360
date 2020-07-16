from django.db import models
from users.models import CustomUser

# Create your models here.

class Document(models.Model):
    """Document model"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
