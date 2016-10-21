from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task(name='shrt.send_email_task')
def send_email_task(subject, message):
    print("I'm in again")
    send_mail(
        subject, 'text', settings.MAIL_FROM,
        settings.MAIL_TO, html_message=message
    )