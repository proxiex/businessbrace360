from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions, generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from . import models, serializers, permissions
from .helper.email import email_test_congrats, email_success_congrats

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
    permission_classes = (permissions.IsSuperUserOrWriteOnly,)


    def update(self, request, pk):
        """Put view."""

        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        email = request.data.get('email', '')
        phone = request.data.get('phone', '')
        dob = request.data.get('dob', '')
        location = request.data.get('location', '')
        cv = request.data.get('cv', '')
        yrs_of_exp = request.data.get('yrs_of_exp', '')
        status_ = request.data.get('status', '')

        candidate = models.Candidate.objects.filter(id=pk)

        if first_name:
            candidate.update(first_name=first_name)
        
        if last_name:
            candidate.update(last_name=last_name)

        if email:
            candidate.update(email=email)

        if phone:
            candidate.update(phone=phone)

        if dob:
            candidate.update(dob=dob)

        if location:
            candidate.update(location=location)

        if cv:
            candidate.update(cv=cv)

        if yrs_of_exp:
            candidate.update(yrs_of_exp=yrs_of_exp)

        if status_:
            candidate.update(status=status_)
            
            # send email.
            if status_ == 'test-candidate':
                email_test_congrats(email, first_name)
            
            elif status_ == 'succesful-candidate':
                email_success_congrats(email, first_name)

        queryset = models.Candidate.objects.filter(id=pk)
        candidate = serializers.CandidateSerializer(queryset, many=True)
        return Response(candidate.data, status=status.HTTP_200_OK)



class TestResultsViewSet(viewsets.ModelViewSet):
    queryset = models.TestResult.objects.all()
    serializer_class = serializers.TestResultsSerializer
    permission_classes = (AllowAny,)

    def update(self, request, pk):
        """Put view."""

        score = request.data.get('score', '')
        status_ = request.data.get('status', '')

        test_result = models.TestResult.objects.filter(id=pk)

        if score:
            test_result.update(score=score)

        if status_:
            test_result.update(status=status_)
