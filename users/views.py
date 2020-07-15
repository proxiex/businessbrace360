"""Users views."""

from .models import CustomUser
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from .serializers import TokenSerializer, UserSerializer
from users.helpers.decorators import validate_user_login

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    """Login view.

    POST auth/login/
    """

    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @validate_user_login
    def post(self, request, *args, **kwargs):
        """Post view."""
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer_class = TokenSerializer(
                data={
                    "token": jwt_encode_handler(
                        jwt_payload_handler(user))
                })
            serializer_class.is_valid()
            return Response(serializer_class.data)
        error_msg = {"error": "Invalid login credentials!"}
        return Response(error_msg, status=status.HTTP_401_UNAUTHORIZED)
