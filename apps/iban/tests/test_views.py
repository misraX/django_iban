# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse, resolve
from django.test import TestCase, RequestFactory, Client

from ..factories import UserFactory, IBANAccountFactory
from ..views import (
    IBANListView, IBANDetailView, IBANDeleteView, IBANUpdateView,
    IBANCreateView
)


class IBANBaseViewTestCaseMixin(object):
    """
    Base test methods for IBAN Views.
    """

    def test_view_url(self):
        """
        Testing url, resolver and view name.
        """
        url = resolve(self.url)
        view = self.view
        self.assertEquals(url.func.__name__, view.__name__)

    def iban_view(self):
        """
        Base Authorized user request for all the urls.
        """
        request = self.factory.get(self.url)
        request.user = self.user
        return request

    def login_required_iban_view(self):
        """
        Anonymous GET request, should always returns redirect
        with `?next={reverse_url}` to `setting.LOGIN_URL`.
        """
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.redirect)
        # test settings login url
        self.assertRedirects(response, settings.LOGIN_URL + '?next={}'.format(self.url))

    def authorized_update_delete_view(self):
        """
        Authorized user who didn't create the IBANAccount
        instance will get `403` not authorized.
        """
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        self.assertNotEquals(response.status_code, 200)
        # fail with 403, the user is not who created IBANAccountObject object.
        self.assertEquals(response.status_code, 403)

    def authorized_user_who_created_ibanaccount_iban_view(self):
        """
        Authorized user who created the IBANAccount instance
        should always get `200` success.
        """
        request = self.iban_view()
        request.user = self.iban_account.created_by
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        self.assertEquals(response.status_code, 200)
        if self.template_name:
            self.assertEquals(response.template_name[0], self.template_name)


class IBANListViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserFactory()
        self.view = IBANListView
        self.url = reverse('iban_list')
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_list.html'

    def test_login_required_iban_list_view(self):
        return self.login_required_iban_view()

    def test_authorized_iban_list_view(self):
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name[0], self.template_name)


class IBANDetailViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserFactory()
        self.iban_account = IBANAccountFactory()
        self.view = IBANDetailView
        self.url_kwarg = {'pk': self.iban_account.id}
        self.url = reverse('iban:iban_detail', kwargs=self.url_kwarg)
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_detail.html'

    def test_login_required_iban_detail_view(self):
        return self.login_required_iban_view()

    def test_authorized_iban_detail_view(self):
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        self.assertEquals(response.status_code, 200)


class IBANCreateViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserFactory()
        self.iban_account = IBANAccountFactory()
        self.view = IBANCreateView
        self.url = reverse('iban:iban_create')
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_form.html'

    def test_login_required_iban_create_view(self):
        return self.login_required_iban_view()

    def test_authorized_iban_create_view(self):
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)


class IBANDeleteViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserFactory()
        self.iban_account = IBANAccountFactory()
        self.view = IBANDeleteView
        self.url_kwarg = {'pk': self.iban_account.id}
        self.url = reverse('iban:iban_delete', kwargs=self.url_kwarg)
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = None

    def test_login_required_delete_view(self):
        return self.login_required_iban_view()

    def test_authorized_iban_delete_view(self):
        return self.authorized_update_delete_view()

    def test_authorized_user_who_created_ibanaccount_iban_view(self):
        return self.authorized_user_who_created_ibanaccount_iban_view()


class IBANUpdateViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserFactory()
        self.iban_account = IBANAccountFactory()
        self.view = IBANUpdateView
        self.url_kwarg = {'pk': self.iban_account.id}
        self.url = reverse('iban:iban_update', kwargs=self.url_kwarg)
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_form.html'

    def test_login_required_delete_view(self):
        return self.login_required_iban_view()

    def test_authorized_iban_delete_view(self):
        return self.authorized_update_delete_view()

    def test_authorized_user_who_created_ibanaccount_iban_view(self):
        return self.authorized_user_who_created_ibanaccount_iban_view()
