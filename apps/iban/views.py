# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import HttpResponse
from django.views.generic import (
    ListView, DetailView, DeleteView, UpdateView, CreateView
)

from apps.core.views import BaseLoginRequiredMixin
from .models import IBANAccount


class IBANBaseSingleObjectView(object):
    model = IBANAccount
    # use the active manager as the default manager.
    queryset = IBANAccount.is_active.all()
    context_object_name = 'iban_account_item'


class IBANBaseSingleObjectUpdateCreateView(IBANBaseSingleObjectView):
    fields = ['first_name', 'last_name', 'iban', ]
    template_name = 'ibanaccount_form.html'


class IBANListView(BaseLoginRequiredMixin, IBANBaseSingleObjectView, ListView):
    paginate_by = 2
    context_object_name = 'iban_account_list'
    template_name = 'ibanaccount_list.html'


class IBANDetailView(BaseLoginRequiredMixin, IBANBaseSingleObjectView, DetailView):
    template_name = 'ibanaccount_detail.html'


class IBANDeleteView(BaseLoginRequiredMixin, IBANBaseSingleObjectView, DeleteView):
    success_url = '/'
    template_name = 'ibanaccount_delete.html'

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)
        return super(IBANDeleteView, self).dispatch(request, *args, **kwargs)


class IBANCreateView(BaseLoginRequiredMixin, IBANBaseSingleObjectUpdateCreateView, CreateView):

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(IBANCreateView, self).form_valid(form)


class IBANUpdateView(BaseLoginRequiredMixin, IBANBaseSingleObjectUpdateCreateView, UpdateView):

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(IBANUpdateView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)
        return super(IBANUpdateView, self).dispatch(request, *args, **kwargs)
