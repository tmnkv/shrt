from random import SystemRandom, choice
from string import ascii_letters as letters
from string import digits

from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse

from core.models import URL
from core.forms import UrlCreateForm
from core.mixins import InvalidMixin


class IndexView(TemplateView):
    template_name = 'core/index.html'


class UrlCreateView(InvalidMixin, CreateView):
    model = URL
    form_class = UrlCreateForm

    def form_valid(self, form):
        primary_url = form.cleaned_data['primary']
        url = URL.objects.create()
        url.primary = primary_url
        url.shorten = self.generate_short_link()
        url.save()
        return JsonResponse({
            'shorten' : url.shorten
        })

    def generate_short_link(self):
        link = 'http://sh.idaproject.com/' + ''.join(SystemRandom().choice(letters + digits) for _ in range(7))
        if URL.objects.filter(shorten=link).exists():
            link = generate_short_link()
        return link
