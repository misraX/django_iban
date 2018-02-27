# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import HttpResponse
from django.views import View

from apps.core.views import BaseLoginRequiredMixin


class IBANListView(BaseLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Base list view')


class IBANDetailView(BaseLoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Base detail view')


class IBANDeleteView(BaseLoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Base delete view')


class IBANUpdateView(BaseLoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Base iban update view')
