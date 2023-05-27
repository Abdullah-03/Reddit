from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    karma = models.PositiveIntegerField(verbose_name="user karma", default=0, blank=True)
