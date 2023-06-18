from django.urls import path, re_path

from .views import tweet_list, create_tweet, feed_list

app_name = "articles"
urlpatterns = [
    path("list/", tweet_list),
    # re_path(r"^list/(?:(?P<username>[\w-]+)/)?$", tweet_list),
    path("list/<str:username>/", tweet_list),
    path("create/", create_tweet, name="create"),
    path("feed/", feed_list, name="feed"),
]
