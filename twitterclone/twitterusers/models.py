from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    tag = models.CharField(max_length=50)
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    # following = models.ManyToManyField("self")

    def __str__(self):
        return self.tag