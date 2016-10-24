from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task(name='send_email_task')
def send_email_task(subject, message):
    send_mail(
        subject, 'text', settings.MAIL_FROM,
        settings.MAIL_TO, html_message=message
    )
