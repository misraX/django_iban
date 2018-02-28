# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.views.generic import (
    ListView, DetailView, DeleteView, UpdateView, CreateView
)

from .models import IBANAccount


class IBANBaseSingleObjectView(LoginRequiredMixin):
    """
    Extends `LoginRequiredMixin` and handling the base
    configuration for generic views.
    """
    model = IBANAccount
    # use the active manager as the default manager.
    queryset = IBANAccount.is_active.all()
    redirect_field_name = 'redirect_to'
    context_object_name = 'iban_account_item'


class IBANBaseSingleObjectUpdateCreateView(IBANBaseSingleObjectView):
    """
    Extends `IBANBaseSingleObjectView` to handel form fields and
    templates for Create and Update views.
    """
    fields = ['first_name', 'last_name', 'iban', ]
    template_name = 'ibanaccount_form.html'


class IBANListView(IBANBaseSingleObjectView, ListView):
    """
    List all IBAN instances
    """
    paginate_by = 10
    context_object_name = 'iban_account_list'
    template_name = 'ibanaccount_list.html'


class IBANDetailView(IBANBaseSingleObjectView, DetailView):
    """
    `IBANAccount` detail view.
    """
    template_name = 'ibanaccount_detail.html'


class IBANDeleteView(IBANBaseSingleObjectView, DeleteView):
    """
    `IBANAccount` delete view.
    """
    success_url = '/'
    template_name = 'ibanaccount_delete.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Preventing manipulations operations over the model
        instance and allowing it only for users who created it.
        :param request: HttpRequest
        :param args:
        :param kwargs:
        :return: HttpResponse
        """
        if self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)
        return super(IBANDeleteView, self).dispatch(request, *args, **kwargs)


class IBANCreateView(IBANBaseSingleObjectUpdateCreateView, CreateView):

    def form_valid(self, form):
        """
        Auto assign the form model instance ForeignKey
        field `created_by` with the request.user.
        :param form: ModelForm
        :return: HttpResponseRedirect
        """
        form.instance.created_by = self.request.user
        return super(IBANCreateView, self).form_valid(form)


class IBANUpdateView(IBANBaseSingleObjectUpdateCreateView, UpdateView):

    def form_valid(self, form):
        """
        Auto assign the form model instance ForeignKey
        field `created_by` with the request.user.
        :param form: ModelForm
        :return: HttpResponseRedirect
        """
        form.instance.created_by = self.request.user
        return super(IBANUpdateView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        Preventing manipulations operations over the model
        instance and allowing it only for users who created it.
        :param request: HttpRequest
        :param args:
        :param kwargs:
        :return: HttpResponse
        """
        if self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)
        return super(IBANUpdateView, self).dispatch(request, *args, **kwargs)
