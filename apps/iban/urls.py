# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    IBANDetailView, IBANDeleteView, IBANUpdateView
)

urlpatterns = [
    # iban detail url
    # TODO:: will be changed to uuid detail regex.
    url(r'^detail/$', IBANDetailView.as_view(), name='iban_detail'),
    # iban update url
    # TODO:: will be changed to update/<uuid>/$
    url(r'^update/$', IBANUpdateView.as_view(), name='iban_update'),
    # iban delete url
    url(r'^delete/$', IBANDeleteView.as_view(), name='iban_update'),
]
