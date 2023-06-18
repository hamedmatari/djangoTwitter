from django.urls import path
from .views import *

urlpatterns = [
    path("follow/<str:username>/", follow_user, name="follow_user"),
    path("unfollow/<str:username>/", unfollow_user, name="unfollow_user"),
    path("followers/", followers_list, name="followers"),
    path("following/", following_list, name="following"),
]
