from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.contrib.auth.models import User


# @login_required
def tweet_list(request):
    tweets = Tweet.objects.all()
    tweet_data = [
        {"id": tweet.id, "content": tweet.content, "author": tweet.author.username}
        for tweet in tweets
    ]
    return JsonResponse({"tweets": tweet_data})


@login_required
def create_tweet(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            tweet = Tweet.objects.create(content=content, author=request.user)
            return JsonResponse({"success": True, "tweet_id": tweet.id})
        else:
            return JsonResponse({"success": False, "error": "Content is required."})
    else:
        return JsonResponse({"success": False, "error": "Invalid request method."})
