from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUserModel(AbstractUser):
    """ Table/model for store User information """

    age = models.PositiveIntegerField(null=True, blank=True)
    profession = models.CharField(max_length=127, null=True, blank=True)



