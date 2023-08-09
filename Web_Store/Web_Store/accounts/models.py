from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_pics/'
    )



