from django.urls import path

from .views import tweet_list, create_tweet

app_name = "articles"
urlpatterns = [
    path("list/", tweet_list),
    path("create/", create_tweet, name="create"),
    # path('<slug:slug>/', article_detail_view, name='detail'),
]
