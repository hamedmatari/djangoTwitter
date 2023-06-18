from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.contrib.auth import login


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if request.path_info.startswith("/login/"):
            response = get_response(request)
            return response

        # if "auth" in request.headers and request.headers["auth"] == "manHamedHastam":
        if "auth" in request.headers:
            username = cache.get(request.headers["auth"])
            if username is not None:
                request.user = username
                response = get_response(request)
                return response

        raise PermissionDenied()

    return middleware
