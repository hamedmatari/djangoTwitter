from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

User = get_user_model()


@require_http_methods(["POST"])
def follow_user(request, username):
    if request.method == "POST":
        user_to_follow = get_object_or_404(User, username=username)
        request.user.following.add(user_to_follow)
        return JsonResponse({"status": "followed successfully"})


@require_http_methods(["POST"])
def unfollow_user(request, username):
    if request.method == "POST":
        user_to_unfollow = get_object_or_404(User, username=username)
        request.user.following.remove(user_to_unfollow)
        return JsonResponse({"status": "removed successfully"})


@require_http_methods(["GET"])
def following_list(request):
    if request.method == "GET":
        following_list = request.user.following.all()
        following_list_json = [following.username for following in following_list]
        return JsonResponse({"following_list": following_list_json})


@require_http_methods(["GET"])
def followers_list(request):
    if request.method == "GET":
        followers_list = request.user.followers.all()
        followers_list_json = [follower.username for follower in followers_list]
        return JsonResponse({"followers_list": followers_list_json})
