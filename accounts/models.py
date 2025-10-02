from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        blank=True,
        null=True
    )
    phone = models.CharField(max_length=15, blank=True, null=True)