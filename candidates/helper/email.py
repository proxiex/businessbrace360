"""Email module."""

from django.utils import timezone
from datetime import timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mass_mail
from candidates.models import Candidate


def email_test_congrats(email, first_name):
    """Email booking report to user."""
    subject, from_email, to = 'Regarding your application to Businessbrace360', 'noreply@syneinc.com', email
    html_content = render_to_string('emails/test_congrats.html', {'first_name': first_name})
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()