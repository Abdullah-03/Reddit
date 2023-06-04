from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])


class PostVote(models.Model):  # stores all user upvotes,downvotes on a post
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="votes"
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="votes"
    )
    vote = models.IntegerField()

    def switch_vote(self):  # if user casts a different vote changes stored vote to the new one
        self.vote = -self.vote
        self.save()

    class Meta:
        constraints = [models.UniqueConstraint(fields=['post', 'user'], name="post-user post interaction unique")]


class PostComment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments"
    )
    comment = models.TextField()

