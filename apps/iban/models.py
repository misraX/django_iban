# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from localflavor.generic.models import IBANField

from apps.core.models import AbstractBaseModel


@python_2_unicode_compatible
class IBANAccount(AbstractBaseModel):
    """
    IBANAccount
    :first_name `CharField` required.
    :las_name `CharField` required.
    :active `BooleanField` required, with True as default.
    :created_by `ForeignKey` required, User instance relation.
    :iban `IBANField` required.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    iban = IBANField(verbose_name='IBAN')

    def __str__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )
