# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from ..models import AbstractBaseModel


class AbstractBaseModelTestCase(TestCase):
    def setUp(self):
        self.abstract_class = AbstractBaseModel

    def test_is_abstract(self):
        model = self.abstract_class

        self.assertEquals(model._meta.abstract, True)
