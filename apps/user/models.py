from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.user.managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
