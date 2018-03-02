# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet


class ActiveManager(QuerySet):
    """
    Filter by the active accounts, for better queries performance.
    Only the `superuser` can `activate` or `deactivate` the account.
    """

    def active(self):
        return self.filter(active=True)

    def not_active(self):
        return self.filter(active=False)
