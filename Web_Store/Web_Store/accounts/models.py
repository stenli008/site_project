from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_pics/'
    )



