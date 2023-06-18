from django.urls import path, re_path

from .views import tweet_list, create_tweet

app_name = "articles"
urlpatterns = [
    path("list/", tweet_list),
    re_path(r"^list/(?:(?P<username>[\w-]+)/)?$", tweet_list),
    path("list/<str:username>/", tweet_list),
    # path("list/<str:username>/<int:tweet_id>/", tweet_list),
    path("create/", create_tweet, name="create"),
]
