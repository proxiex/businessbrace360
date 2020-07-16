from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions, generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from . import models, serializers, permissions

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    permission_classes = (AllowAny,)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
    permission_classes = (permissions.IsSuperUserOrWriteRetriveOnly,)


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = models.PersonalInfo.objects.all()
    serializer_class = serializers.PersonalInfoSerializer
    permission_classes = (AllowAny,)


class onBoardingStatusViewSet(viewsets.ModelViewSet):
    queryset = models.onBoardingStatus.objects.all()
    serializer_class = serializers.onBoardingStatus
    permission_classes = (AllowAny,)
