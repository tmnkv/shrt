from random import SystemRandom, choice
from string import ascii_letters as letters
from string import digits

from django.views.generic import TemplateView, ListView, CreateView, RedirectView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from core.models import URL
from core.forms import UrlCreateForm
from core.mixins import InvalidMixin


SITE_URL = 'http://sh.idaproject.com/'


class IndexView(TemplateView):
    template_name = 'core/index.html'


class UrlListView(ListView):
    model = URL


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
        link = SITE_URL + ''.join(SystemRandom().choice(letters + digits) for _ in range(7))
        if URL.objects.filter(shorten=link).exists():
            link = self.generate_short_link()
        return link


class UrlRedirectView(RedirectView):

    def get_redirect_url(self, url, *args, **kwargs):
        shorten = SITE_URL + url
        url = get_object_or_404(URL, shorten=shorten)
        url.counter_plus()
        return url.primary
