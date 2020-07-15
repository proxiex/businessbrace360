from django.db import models
from jobs.models import Job

# Create your models here.

class Candidate(models.Model):
    """Candidates model"""

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)
    phone = models.CharField(blank=False, max_length=255)
    dob = models.CharField(blank=False, max_length=255)
    location = models.CharField(blank=False, max_length=255)
    cv = models.FileField(blank=False, null=True)
    yrs_of_exp = models.CharField(blank=False, max_length=255)
    created_at = models.DateTimeField(
        auto_now_add=True, 
        auto_now=False,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now_add=False, 
        auto_now=True,
        verbose_name='Updated At'
    )
    status = models.CharField(
      choices = (('job-applicant', 'Job Applicant'), ('test-candidate', 'Test Candidate'), ('succesful-candidate', 'Succesful Candidate'),),
      max_length = 100
    )

    def __str__(self):
      return f"{self.pk})  {self.first_name } {self.last_name}"


class TestResult(models.Model):
    """Candidates test result."""
    
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    score = models.FloatField(blank=False, default=0.0, max_length=255)
    status = models.CharField(
      choices = (('fail', 'Failed'), ('pass', 'Passed'), ('retry', 'Retry'),),
      max_length = 100
    )

    def __str__(self):
      return f"{self.pk})  {self.candidate } {self.score} - {self.status}"