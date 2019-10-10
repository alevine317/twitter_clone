from django.db import models


class Notifications(models.Model):
    has_notification = models.BooleanField()

    def __str__(self):
        return self.name