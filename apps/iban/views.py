# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.views.generic import (
    ListView, DetailView, DeleteView, UpdateView, CreateView
)

from .forms import IBANAccountModelForm
from .models import IBANAccount


class IBANBaseSingleObjectView(LoginRequiredMixin):
    """
    Extends `LoginRequiredMixin` to handle the base
    configuration for generic List, Detail views.
    """
    model = IBANAccount
    # use the active manager as the default manager.
    queryset = IBANAccount.is_active.all()
    context_object_name = 'iban_account_item'
    redirect_field_name = 'redirect_to'


class IBANBaseSingleObjectUpdateCreateView(LoginRequiredMixin):
    """
    Extends `LoginRequiredMixin` to handle the base
    configuration for generic Update, Create views.
    """
    model = IBANAccount
    context_object_name = 'iban_account_item'
    template_name = 'ibanaccount_form.html'
    form_class = IBANAccountModelForm
    redirect_field_name = 'redirect_to'


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
        super(IBANDeleteView, self).dispatch(request, *args, **kwargs)
        if self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)


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
        super(IBANUpdateView, self).dispatch(request, *args, **kwargs)
        if self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)
