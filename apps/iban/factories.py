# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

import factory
from django.contrib.auth.models import User

from .models import IBANAccount


class UserFactory(factory.django.DjangoModelFactory):
    """
    Build a User instance with factory.
    """

    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    email = factory.Faker('email')


class IBANAccountFactory(factory.django.DjangoModelFactory):
    """
    Build an IBANAccount instance with factory.
    """

    class Meta:
        model = IBANAccount

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    iban = 'DE89 3704 0044 0532 0130 00'
    created_by = factory.SubFactory(UserFactory)
    created_at = datetime.datetime.now()
    updated_at = created_at
