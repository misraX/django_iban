# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

import factory
from django.test import TestCase

from ..factories import IBANAccountFactory, UserFactory
from ..models import IBANAccount


class IBANAccountTest(TestCase):
    def setUp(self):
        self.iban_account_1 = IBANAccountFactory(
            first_name='name1',
            last_name='last1',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=factory.SubFactory(UserFactory),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        self.iban_account_2 = IBANAccountFactory(
            first_name='first2',
            last_name='last2',
            iban='DE89 3704 0044 0532 0130 00',
            created_by=factory.SubFactory(UserFactory),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            active=False
        )

    def test_iban_account_active_manager(self):
        self.assertQuerysetEqual(IBANAccount.objects.active(), ['<IBANAccount: name1, last1>'])

    def test_iban_account_not_active_manager(self):
        self.assertQuerysetEqual(IBANAccount.objects.not_active(), ['<IBANAccount: first2, last2>'])

    def test_iban_account_str_method(self):
        self.assertEquals(self.iban_account_1.__str__(), 'name1, last1')

    def test_iban_account_get_absolute_url(self):
        self.assertEquals(self.iban_account_1.get_absolute_url(), '/iban/{pk}/'.format(
            pk=self.iban_account_1.id)
                          )
