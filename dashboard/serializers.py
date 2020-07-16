"""Dashboard serializer."""

import os
from rest_framework import serializers
from . import models


class DocumentSerializer(serializers.ModelSerializer):
    """Document serialzers class."""

    class Meta:
        """Meta class."""

        model = models.Document
        fields = "_all_"


class CertificateSerializer(serializers.ModelSerializer):
    """Certificate serialzers class."""

    class Meta:
        """Meta class."""

        model = models.Certificate
        fields = '__all__'


class PersonalInfoSerializer(serializers.ModelSerializer):
    """PersonalInfo serialzers class."""

    class Meta:
        """Meta class."""

        model = models.PersonalInfo
        fields = '__all__'

class onBoardingStatus(serializers.ModelSerializer):
    """onBoardingStatus serialzers class."""

    class Meta:
        """Meta class."""

        model = models.onBoardingStatus
        fields = '__all__'
