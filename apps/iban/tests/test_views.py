# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client

from ..factories import UserFactory, IBANAccountFactory
from ..models import IBANAccount
from ..views import (
    IBANListView, IBANDetailView, IBANDeleteView, IBANUpdateView,
    IBANCreateView
)


class IBANBaseViewTestCaseMixin(TestCase):
    """
    Base test methods for IBAN Views.
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserFactory()
        self.iban_account = IBANAccountFactory()

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

    def post_response(self):
        response = self.client.post(self.url)
        return response

    def login_required_view_post(self):
        response = self.post_response()
        self.assertEquals(response.status_code, 302)
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
        super(IBANListViewTestCaseMixin, self).setUp()
        self.view = IBANListView
        self.url = reverse('iban_list')
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_list.html'

    def test_login_required_iban_list_view(self):
        return self.login_required_iban_view()

    def test_login_required_iban_list_view_post(self):
        return self.login_required_view_post()

    def test_authorized_iban_list_view(self):
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name[0], self.template_name)

    def test_authorized_user_post_request(self):
        request = self.factory.post(self.url)
        request.user = self.user
        response = self.view.as_view(template_engine=self.template_name)(request)
        response.client = self.client
        # not allowed
        self.assertEquals(response.status_code, 405)


class IBANDetailViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        super(IBANDetailViewTestCaseMixin, self).setUp()
        self.view = IBANDetailView
        self.url_kwarg = {'pk': self.iban_account.id}
        self.url = reverse('iban:iban_detail', kwargs=self.url_kwarg)
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_detail.html'

    def test_login_required_iban_detail_view(self):
        return self.login_required_iban_view()

    def test_login_required_iban_detail_view_post(self):
        return self.login_required_view_post()

    def test_authorized_iban_detail_view(self):
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        self.assertEquals(response.status_code, 200)

    def test_authorized_user_post_request(self):
        request = self.factory.post(self.url)
        request.user = self.user
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        # not allowed
        self.assertEquals(response.status_code, 405)


class IBANCreateViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        super(IBANCreateViewTestCaseMixin, self).setUp()
        self.view = IBANCreateView
        self.url = reverse('iban:iban_create')
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_form_create.html'

    def test_login_required_iban_create_view(self):
        return self.login_required_iban_view()

    def test_login_required_iban_create_view_post(self):
        return self.login_required_view_post()

    def test_authorized_iban_create_view(self):
        request = self.iban_view()
        response = self.view.as_view(template_engine=self.template_name)(request)
        response.client = self.client
        # allowed for authorized user
        self.assertEquals(response.status_code, 200)

    def test_authorized_user_post_request(self):
        request = self.factory.post(self.url)
        request.user = self.user
        response = self.view.as_view(template_engine=self.template_name)(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)

    def test_create_with_authorized(self):
        user1 = User.objects.create_user('testuser', 'test@mail.com', 'testpass')
        self.client.login(username='testuser', password='testpass')
        # test with iban already exist
        res = self.client.post('/iban/add/', {'first_name': 'Randall Munroe', 'last_name': 'randall-munroe',
                                              'iban': self.iban_account.iban})
        # iban already exist validation error
        self.assertFalse(res.context_data['form'].is_valid())
        # IBAN already exist
        form_error = [error_code for error_code in res.context_data['form'].errors['iban']]
        self.assertEquals(form_error, ['IBAN already exist'])
        res = self.client.post('/iban/add/', {'first_name': 'Randall Munroe', 'last_name': 'randall-munroe',
                                              'iban': 'RO49 AAAA 1B31 0075 9384 0000'})
        # saved and redirect to '/iban/<pk>/'
        iban_account_pk = IBANAccount.objects.get(iban__exact='RO49 AAAA 1B31 0075 9384 0000')
        self.assertRedirects(res, reverse('iban:iban_detail', kwargs={'pk': iban_account_pk.id}))


class IBANDeleteViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        super(IBANDeleteViewTestCaseMixin, self).setUp()
        self.view = IBANDeleteView
        self.url_kwarg = {'pk': self.iban_account.id}
        self.url = reverse('iban:iban_delete', kwargs=self.url_kwarg)
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = None

    def test_login_required_delete_view(self):
        return self.login_required_iban_view()

    def test_login_required_iban_delete_view_post(self):
        return self.login_required_view_post()

    def test_authorized_iban_delete_view(self):
        return self.authorized_update_delete_view()

    def test_authorized_user_who_created_ibanaccount(self):
        return self.authorized_user_who_created_ibanaccount_iban_view()

    def test_authorized_user_post_request(self):
        request = self.factory.post(self.url)
        request.user = self.user
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        self.assertEquals(response.status_code, 403)


class IBANUpdateViewTestCaseMixin(IBANBaseViewTestCaseMixin, TestCase):
    def setUp(self):
        super(IBANUpdateViewTestCaseMixin, self).setUp()
        self.view = IBANUpdateView
        self.url_kwarg = {'pk': self.iban_account.id}
        self.url = reverse('iban:iban_update', kwargs=self.url_kwarg)
        self.redirect = '/accounts/login/?next={}'.format(self.url)
        self.template_name = 'ibanaccount_form_update.html'
        self.data = {
            'first_name': 'first',
            'second_name': 'second',
            'iban': self.iban_account.iban
        }

    def test_login_required_iban_update_view(self):
        return self.login_required_iban_view()

    def test_authorized_iban_update_view(self):
        return self.authorized_update_delete_view()

    def test_authorized_user_who_created_ibanaccount(self):
        return self.authorized_user_who_created_ibanaccount_iban_view()

    def test_login_required_post_iban_update_view(self):
        return self.login_required_view_post()

    def test_authorized_user_post_request(self):
        request = self.factory.post(self.url)
        request.user = self.user
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        response.client = self.client
        self.assertEquals(response.status_code, 403)

    def test_authorized_user_who_created_ibanaccount_with_post(self):
        request = self.factory.post(self.url, data=self.data)
        request.user = self.iban_account.created_by
        response = self.view.as_view(template_engine=self.template_name)(request, **self.url_kwarg)
        self.assertEquals(response.status_code, 200)
