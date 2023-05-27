from django.contrib.auth import get_user_model
from django.db import models

from profiles.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    karma = models.IntegerField(verbose_name="post karma", default=1)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="posts"
    )

