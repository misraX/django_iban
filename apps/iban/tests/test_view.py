# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, resolve
from django.test import TestCase, RequestFactory, Client

from ..views import IBANListView


class IBANAccountBaseViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = None
        self.url = None
        self.redirect = '/accounts/login/?redirect_to={}'.format(self.url)


class IBANAccountListViewTestCase(IBANAccountBaseViewTestCase, TestCase):

    def setUp(self):
        super(IBANAccountListViewTestCase, self).setUp()
        self.view = IBANListView
        self.url = reverse('iban_list')
        self.redirect = '/accounts/login/?redirect_to={}'.format(self.url)

    def test_iban_account_list_view_url(self):
        """
        Testing url.
        """
        url = resolve(self.url)
        view = self.view
        self.assertEquals(url.func.__name__, view.__name__)

    def test_iban_account_list_view(self):
        """
        Testing the list view with an authenticated user.
        """
        request = self.factory.get(reverse('iban_list'))
        user = User(
            username='user', email='x@x.com', password='password'
        )
        request.user = user
        view = self.view.as_view(template_name='ibanaccount_list.html')
        response = view(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name[0], 'ibanaccount_list.html')

    def test_login_required_iban_account_list_view(self):
        """
        Check anonymous GET request.
        """
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.redirect)
        # test settings login url
        self.assertRedirects(response, settings.LOGIN_URL + '?redirect_to={}'.format(self.url))
