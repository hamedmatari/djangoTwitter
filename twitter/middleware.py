from django.core.exceptions import PermissionDenied


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if "auth" in request.headers and request.headers["auth"] == "manHamedHastam":
            response = get_response(request)
            return response

        raise PermissionDenied()

    return middleware
