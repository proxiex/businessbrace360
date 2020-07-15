"""Users serializer."""

import os
from django.conf import settings
from rest_framework import serializers
from . import models


class JobSerializer(serializers.ModelSerializer):
    """Job serialzers class."""

    class Meta:
        """Meta class."""

        model = models.Job
        fields = [
            'title',
            'location',
            'description',
            'is_active',
            'created'
        ]
