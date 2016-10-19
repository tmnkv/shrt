from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(
        regex=r'^admin/',
        view=admin.site.urls
    ),
    url(
        regex=r'^',
        view=include('core.urls')
    )
]
