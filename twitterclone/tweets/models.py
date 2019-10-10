from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from django.utils import timezone


class Tweet(models.Model):
    tweet_by = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE, null=True, blank=True)
    tweet_text = models.CharField(max_length=140)
    tweet_time = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.tweet_text