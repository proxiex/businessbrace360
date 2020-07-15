from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from . import models, serializers, permissions

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class JobViewSet(viewsets.ModelViewSet):
    """Job model viewSet."""

    serializer_class = serializers.JobSerializer
    queryset = models.Job.objects.all()
    permission_classes = [permissions.IsSuperUserOrReadOnly, ]

