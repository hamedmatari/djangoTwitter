from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse

from .models import Tweet

User = get_user_model()


@require_GET
def tweet_list(request):
    username = request.GET.get("username")
    if username is None:
        tweets = Tweet.objects.filter(author=request.user)
    else:
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(author=user)

    tweet_data = [
        {"id": tweet.id, "content": tweet.content, "author": tweet.author.username}
        for tweet in tweets
    ]
    return JsonResponse({"tweets": tweet_data})


@require_POST
def create_tweet(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            tweet = Tweet.objects.create(content=content, author=request.user)
            return JsonResponse({"success": True, "tweet_id": tweet.id})
        else:
            return JsonResponse({"success": False, "error": "Content is required."})
    else:
        return JsonResponse(
            {"success": False, "error": "Invalid request method."}, status=405
        )


@require_GET
def feed_list(request):
    tweets = Tweet.objects.filter(author__in=request.user.following.all())
    tweet_data = [
        {"id": tweet.id, "content": tweet.content, "author": tweet.author.username}
        for tweet in tweets
    ]
    return JsonResponse({"tweets": tweet_data})


@require_POST
def like_tweet(request):
    tweet_id = request.POST.get("tweet_id")

    if tweet_id is None:
        return JsonResponse({"success": False, "error": "Tweet id is required."})

    tweet = Tweet.objects.get(id=tweet_id)
    tweet.liked_users.add(request.user)
    return JsonResponse(
        {"success": f"you liked tweet id:{tweet_id} , name: {tweet.content}"}
    )


@require_POST
def unlike_tweet(request):
    tweet_id = request.POST.get("tweet_id")

    if tweet_id is None:
        return JsonResponse({"success": False, "error": "Tweet id is required."})

    tweet = Tweet.objects.get(id=tweet_id)
    tweet.liked_users.remove(request.user)
    return JsonResponse(
        {"success": f"you unliked tweet id:{tweet_id} , name: {tweet.content}"}
    )


@require_GET
def get_likes(request):
    tweets = Tweet.objects.filter(liked_users__username=request.user.username)

    # TODO continue from here
