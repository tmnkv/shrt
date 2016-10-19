from django.views.generic import TemplateView

from core.models import URL


class IndexView(TemplateView):
    template_name = 'core/index.html'
