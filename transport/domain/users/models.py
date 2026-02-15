from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices(models.TextChoices):
    USER = "USER"
    ADMIN = "ADMIN"


class User(AbstractUser):
    role = models.CharField(
        max_length=10, choices=RoleChoices.choices, default=RoleChoices.USER
    )

    def __str__(self):
        return self.username
