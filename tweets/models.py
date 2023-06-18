from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]  # Return a truncated version of the tweet content

    class Meta:
        ordering = ["-timestamp"]
