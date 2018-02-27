# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class AbstractBaseModel(models.Model):
    """
    Base model with most used fields.
    :uuid `UUIDField`, defines a unique instance uuid version 4.
    :created_at `DateTimeField`, defines instance creation date.
    :updated_at `DateTimeField`, defines instance updating date.
    """
    uuid = models.UUIDField(default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
