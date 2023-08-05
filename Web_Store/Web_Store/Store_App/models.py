from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_image_size(value):
    max_image_size = 10

    if value.size > max_image_size:
        raise ValidationError(
            f'Profile picture cannot be above {max_image_size} Mbs!'
        )


class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_pics/'
    )
