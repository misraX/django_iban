# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import HttpResponse


class PreventManipulationAccessMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        """
        Preventing manipulations and un authenticated users
        (Anonymous) operations over the model instance and
        allowing it only for authenticated users and only
        for users who created it.

        Checking get_queryset is important to avoid redirecting
        to the same view. After using POST method to delete the
        model instance the request method will fail to redirect
        since the dispatch method will be called with the same
        method and `get_object()` will return Http404 as the object
        have been deleted that will break the dispatch operation
        and fail to Http404 rather than completing the redirection
        of `get_success_url()`.

        :param request: HttpRequest
        :param args: None
        :param kwargs: pk ,url request parameter
        :return: HttpResponse
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.get_queryset() and self.get_object().created_by != self.request.user:
            return HttpResponse('Not authorized', status=403)
        return super(PreventManipulationAccessMixin, self).dispatch(request, *args, **kwargs)
