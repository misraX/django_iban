# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin


class BaseLoginRequiredMixin(LoginRequiredMixin):
    redirect_field_name = 'redirect_to'
