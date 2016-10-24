from django.conf.urls import url

from core.views import IndexView, UrlListView, UrlCreateView, UrlRedirectView


urlpatterns = [
    url(
        regex=r'^$',
        view=IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^add/$',
        view=UrlCreateView.as_view(),
        name='add'
    ),
    url(
        regex=r'^(?P<url>\w{7})/$',
        view=UrlRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^stats/$',
        view=UrlListView.as_view(),
        name='stats'
    ),
]