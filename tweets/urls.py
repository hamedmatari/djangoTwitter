from django.urls import path, re_path

from .views import tweet_list, create_tweet, feed_list, like_tweet, unlike_tweet

app_name = "articles"
urlpatterns = [
    path("list/", tweet_list),
    # re_path(r"^list/(?:(?P<username>[\w-]+)/)?$", tweet_list),
    path("list/<str:username>/", tweet_list),
    path("like/", like_tweet),
    path("unlike/", unlike_tweet),
    path("create/", create_tweet, name="create"),
    path("feed/", feed_list, name="feed"),
]
