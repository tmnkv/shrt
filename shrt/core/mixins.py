from django.http import JsonResponse


class InvalidMixin():

    def form_invalid(self, form):
        print(form)
        return JsonResponse(form.errors, status=404)
