from django.db import models
from account.models import TwitterUser


class Tweet(models.Model):
    content = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(
        TwitterUser, related_name="liked_tweets", blank=True
    )

    def __str__(self):
        return self.content[:50]  # Return a truncated version of the tweet content

    class Meta:
        ordering = ["-timestamp"]
