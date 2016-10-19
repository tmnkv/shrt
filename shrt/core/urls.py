from django.conf.urls import url

from core.views import IndexView


urlpatterns = [
    url(
        regex=r'^$',
        view=IndexView.as_view(),
        name='index'
    ),
]