from __future__ import unicode_literals

from django.test import TestCase

from ..forms import IBANAccountModelForm


class IBANAccountModelFormTestCase(TestCase):
    def setUp(self):
        self.form = IBANAccountModelForm

    def test_form_is_valid(self):
        form = self.form(data={
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'iban': 'DE89 3704 0044 0532 0130 00'
        })
        self.assertEquals(form.is_valid(), True)

    def test_form_is_invalid_first_name_required(self):
        form = self.form(data={
            'first_name': '',
            'last_name': 'mylastname',
            'iban': 'DE89 3704 0044 0532 0130 00'
        })
        self.assertEquals(form.is_valid(), False)
        self.assertTrue(form.has_error('first_name', code='required'))

    def test_form_is_invalid_last_name_required(self):
        form = self.form(data={
            'first_name': 'myfirstname',
            'last_name': '',
            'iban': 'DE89 3704 0044 0532 0130 00'
        })
        self.assertEquals(form.is_valid(), False)
        self.assertTrue(form.has_error('last_name', code='required'))

    def test_form_is_invalid_iban_required(self):
        form = self.form(data={
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'iban': ''
        })
        self.assertEquals(form.is_valid(), False)
        self.assertTrue(form.has_error('iban', code='required'))
