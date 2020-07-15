from django.db import models

# Create your models here.

class Job(models.Model):
    """Job model"""

    title = models.CharField(blank=False, max_length=255)
    location = models.CharField(choices=(('onsite', 'On-site'), ('remote', 'Remote'),), max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    description = models.CharField(blank=False, max_length=255)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%d) %s: %s" % (self.pk, self.title, self.location)