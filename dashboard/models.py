from django.db import models
from user_auth.models import CustomUser

# Create your models here.

class Document(models.Model):
    """Document model"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nda = models.FileField(blank=False, null=True)
    employment_agreement = models.FileField(blank=False, null=True)
    relationship_policy = models.CharField(blank=True, max_length=255)
    company_policy = models.CharField(blank=True, max_length=255)


class Certificate(models.Model):
    """Document model"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    certificate = models.FileField(blank=False, null=True)
    certificate_type = models.CharField(blank=True, max_length=255)


class PersonalInfo(models.Model):
    """Personal infor model"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    marital_status = models.CharField(
        choices=(('married', 'Married'), ('single', 'single'), ('widowed', 'Widowed'),),
        blank=True, max_length=255
    )


class onBoardingStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stage = models.CharField(
        choices=(('personal-info', 'Personal Info'), ('sign-docs', 'Sign Company Docs'), ('upload-cert', 'Upload Certificate'), ('completed', 'Completed')),
        blank=True, max_length=255
    )

