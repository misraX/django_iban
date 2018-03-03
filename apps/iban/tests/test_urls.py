# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from ..factories import IBANAccountFactory
from ..views import IBANDetailView, IBANDeleteView, IBANCreateView, IBANUpdateView, IBANListView


class IABNDetailViewURLTest(TestCase):
    def setUp(self):
        self.iban_pk = IBANAccountFactory().id
        self.url_kwarg = {'pk': self.iban_pk}
        self.url_name = 'iban:iban_detail'
        self.view = IBANDetailView

    def test_url(self):
        url = reverse(self.url_name, kwargs=self.url_kwarg)
        self.assertEquals(url, '/iban/{}/'.format(self.iban_pk))


class IABNDeleteViewURLTest(TestCase):
    def setUp(self):
        self.iban_pk = IBANAccountFactory().id
        self.url_kwarg = {'pk': self.iban_pk}
        self.url_name = 'iban:iban_delete'
        self.view = IBANDeleteView

    def test_url(self):
        url = reverse(self.url_name, kwargs=self.url_kwarg)
        self.assertEquals(url, '/iban/delete/{}/'.format(self.iban_pk))


class IABNUpdateViewURLTest(TestCase):
    def setUp(self):
        self.iban_pk = IBANAccountFactory().id
        self.url_kwarg = {'pk': self.iban_pk}
        self.url_name = 'iban:iban_update'
        self.view = IBANUpdateView

    def test_url(self):
        url = reverse(self.url_name, kwargs=self.url_kwarg)
        self.assertEquals(url, '/iban/update/{}/'.format(self.iban_pk))


class IABNCreateViewURLTest(TestCase):
    def setUp(self):
        self.url_name = 'iban:iban_create'
        self.view = IBANCreateView

    def test_url(self):
        url = reverse(self.url_name)
        self.assertEquals(url, '/iban/add/')


class IABNListViewURLTest(TestCase):
    def setUp(self):
        self.url_name = 'iban_list'
        self.view = IBANListView

    def test_url(self):
        url = reverse(self.url_name)
        self.assertEquals(url, '/')
