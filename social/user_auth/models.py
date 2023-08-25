from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserModel(AbstractUser):
    profilePhoto = models.ImageField(upload_to='dp/', default='dp/default.png')