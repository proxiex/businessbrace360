"""Candidates urls."""

from django.urls import path
from .views import CandidateViewSet, TestResultsViewSet


urlpatterns = [
    path('candidate/', CandidateViewSet.as_view(), name="candidate"),
    path('candidate/test/', TestResultsViewSet.as_view(), name="candidate"),
]
