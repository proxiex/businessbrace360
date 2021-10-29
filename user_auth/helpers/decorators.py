"""User decorators."""

import re
from rest_framework.response import Response
from rest_framework.views import status


def validate_password(password):
    """Validate Password.

    :params: password
    :returns: Boolean
    """
    if re.search(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$", password) is not None:
        return True
    return False


def validate_email(email):
    """Validate Email.

    :params: email
    :returns: Boolean
    """
    if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is not None:
        return True
    return False


def validate_user_login(fn):
    """Validate user login data decorator.

    :returns: fn
    """
    def decorator(*args, **kwargs):

        username = args[0].request.data.get("username", "")
        password = args[0].request.data.get("password", "")
        if not username:
            return Response(
                data={
                    "error": "Username is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not password:
            return Response(
                data={
                    "error": "Password is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorator
