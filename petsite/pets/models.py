from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PetUser(AbstractUser):
    pet = models.CharField(max_length=255)
    friends = models.ArrayField()