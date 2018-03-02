# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from apps.iban.views import IBANListView

urlpatterns = [
    # Home page
    url(r'^$', IBANListView.as_view(), name='iban_list'),
    url(r'^admin/', admin.site.urls),
    # allauth urls.
    url(r'^accounts/', include('allauth.urls')),
    # iban urls.
    url(r'^iban/', include('apps.iban.urls', namespace='iban')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
