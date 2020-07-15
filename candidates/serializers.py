"""Candicates serializer."""

import os
from django.conf import settings
from rest_framework import serializers
from . import models


class CandidateSerializer(serializers.ModelSerializer):
    """Candidate serialzers class."""

    class Meta:
        """Meta class."""

        model = models.Candidate
        fields = [
            'id',
            'job',
            'first_name',
            'last_name',
            'email',
            'phone',
            'location',
            'cv',
            'yrs_of_exp',
            'created_at',
            'status',
        ]


class TestResultsSerializer(serializers.ModelSerializer):
    """Test Results serialzers class."""

    class Meta:
        """Meta class."""

        model = models.TestResult
        fields = [
            'id',
            'candidate',
            'score',
            'status',
        ]