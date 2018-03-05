# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView, DeleteView, UpdateView, CreateView
)

from .auth.mixins import PreventManipulationAccessMixin
from .forms import IBANAccountModelForm
from .models import IBANAccount


class IBANBaseViewConfiguration(object):
    """
    The very basic configuration for IBAN Views.
    """
    model = IBANAccount


class IBANBaseListDetailView(LoginRequiredMixin, IBANBaseViewConfiguration):
    """
    Base List and Detail Views, extends `LoginRequiredMixin`
    and `IBANBaseViewConfiguration` to handle authorization
    and base configuration for generic List, Detail Views.
    """

    # use the active manager as the default manager.
    queryset = IBANAccount.objects.active()


class IANBaseCreateUpdateView(IBANBaseViewConfiguration):
    """
    Base Create and Update Views, extends `IBANBaseViewConfiguration`
    """
    template_name = 'ibanaccount_form.html'
    form_class = IBANAccountModelForm

    def form_valid(self, form):
        """
        Assign the form model instance ForeignKey field
        `created_by` with the request.user.

        :param form: ModelForm
        :return: HttpResponseRedirect
        """
        form.instance.created_by = self.request.user
        return super(IANBaseCreateUpdateView, self).form_valid(form)


class IBANBaseCreateView(LoginRequiredMixin, IANBaseCreateUpdateView):
    """
    Base CreateView extends `LoginRequiredMixin` and
    `IANBaseCreateUpdateView` to handle login required
    Authorization and base View configuration.
    """
    pass


class IBANListView(IBANBaseListDetailView, ListView):
    """
    List all `IBANAccount` instances, with 10 pagination
    limit.
    """
    paginate_by = 10
    context_object_name = 'iban_account_list'
    template_name = 'ibanaccount_list.html'


class IBANDetailView(IBANBaseListDetailView, DetailView):
    """
    Detail an `IBANAccount` instance by `pk`.
    """
    context_object_name = 'iban_account_item'
    template_name = 'ibanaccount_detail.html'


class IBANDeleteView(PreventManipulationAccessMixin,
                     IBANBaseViewConfiguration,
                     DeleteView):
    """
    Delete `IBANAccount` View, extends `PreventManipulationAccessMixin`
    `IANBaseCreateUpdateView` and generic `DeleteView`, a restricted
    View that prevent not only Anonymous users but also Authorized
    users who did not create the model instance from performing any
    operation on the model instance.
    """
    success_url = reverse_lazy('iban_list')
    context_object_name = 'iban_account_item'
    template_name = 'ibanaccount_delete.html'


class IBANCreateView(IBANBaseCreateView, CreateView):
    """
    Create a new IBANAccount instance.
    """
    template_name = 'ibanaccount_form_create.html'


class IBANUpdateView(PreventManipulationAccessMixin,
                     IANBaseCreateUpdateView,
                     UpdateView):
    """
    Update `IBANAccount` View, extends `PreventManipulationAccessMixin`
    `IANBaseCreateUpdateView` and generic `UpdateView`, a restricted
    View that prevent not only Anonymous users but also Authorized
    users from performing any operation on the model instance, unless
    it's owned by the request.user.
    """
    template_name = 'ibanaccount_form_update.html'
