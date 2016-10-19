from django.conf.urls import url

from core.views import IndexView, UrlCreateView


urlpatterns = [
    url(
        regex=r'^$',
        view=IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^add/$',
        view=UrlCreateView.as_view(),
        name='url_add'
    )
]