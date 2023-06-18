from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.contrib.auth import login
from django.contrib.auth.models import User


def auth_middleware(get_response):
    def middleware(request):
        if request.path_info.startswith("/login/"):
            response = get_response(request)
            return response

        # if "auth" in request.headers and request.headers["auth"] == "manHamedHastam":
        if "auth" in request.headers:
            username = cache.get(request.headers["auth"])
            if username is not None:
                user = User.objects.get(username=username)
                request.user = user
                response = get_response(request)
                return response

        raise PermissionDenied()

    return middleware
