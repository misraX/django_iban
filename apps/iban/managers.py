# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ActiveManager(models.Manager):
    """
    Filter by the active accounts, for better queries performance.
    Only the `superuser` can `activate` or `deactivate` the account.
    """

    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)
