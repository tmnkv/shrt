from django.http import JsonResponse
from django.template.loader import render_to_string

from core.tasks import send_email_task


class InvalidMixin:
    def form_invalid(self, form):
        return JsonResponse(form.errors, status=404)


class SendEmailMixin:
    def send_mail(self, subject, template, obj):
        print("I'm in")
        message = render_to_string(template, {'obj': obj})
        print(message)
        send_email_task.delay(subject, message)
