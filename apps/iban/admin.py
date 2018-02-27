# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import IBANAccount


@admin.register(IBANAccount)
class IBANAccountModelAdmin(admin.ModelAdmin):
    pass
