# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.encoding import python_2_unicode_compatible
from localflavor.generic.models import IBANField

from apps.core.models import AbstractBaseModel
from .managers import ActiveManager


@python_2_unicode_compatible
class IBANAccount(AbstractBaseModel):
    """
    IBANAccount

    :first_name `CharField` required.

    :las_name `CharField` required.

    :active `BooleanField` required, with True as default,
             only superusers can activate or deactivate the account.

    :created_by `ForeignKey` required, User instance relation.

    :iban `IBANField` required.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    iban = IBANField(verbose_name='IBAN', use_nordea_extensions=True)

    objects = ActiveManager.as_manager()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'IBAN accounts'

    def __str__(self):
        return '{first_name}, {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    def get_absolute_url(self):
        return reverse('iban:iban_detail', kwargs={'pk': self.id})
