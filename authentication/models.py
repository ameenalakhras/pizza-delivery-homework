from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.TextField(null=True)
