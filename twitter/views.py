from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        print("in log in view")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate a token
            token = generate_token()
            cache.set(token, username)

            # Return the token as a JSON response
            return JsonResponse({"token": token})

    # Invalid credentials or GET request
    return JsonResponse({"error": "Invalid credentials"}, status=401)


def generate_token():
    import secrets

    return secrets.token_hex(16)
