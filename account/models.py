from django.contrib.auth.models import AbstractUser
from django.db import models


class TwitterUser(AbstractUser):
    # Add your custom fields here
    following = models.ManyToManyField(
        "self", blank=True, symmetrical=False, related_name="followers"
    )
