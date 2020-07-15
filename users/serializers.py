"""Users serializer."""

import os
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Users serialzers class."""

    class Meta:
        """Meta class."""

        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = models.CustomUser
        fields = [
            'email',
            'username',
            'password',
        ]


class TokenSerializer(serializers.Serializer):
    """Token data serializer."""

    token = serializers.CharField(max_length=255)
