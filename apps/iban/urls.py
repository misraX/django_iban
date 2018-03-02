# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    IBANDetailView, IBANDeleteView, IBANUpdateView, IBANCreateView
)

urlpatterns = [
    # iban add url
    url(r'add/$', IBANCreateView.as_view(), name='iban_create'),
    # iban detail url
    url(r'^(?P<pk>[0-9]+)/$', IBANDetailView.as_view(), name='iban_detail'),
    # iban update url
    url(r'^update/(?P<pk>[0-9]+)/$', IBANUpdateView.as_view(), name='iban_update'),
    # iban delete url
    url(r'^delete/(?P<pk>[0-9]+)/$', IBANDeleteView.as_view(), name='iban_delete'),
]
