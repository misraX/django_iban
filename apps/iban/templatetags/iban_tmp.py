# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from localflavor.generic.validators import IBAN_COUNTRY_CODE_LENGTH, NORDEA_COUNTRY_CODE_LENGTH

register = template.Library()


@register.filter(name='iban_country_code')
def get_iban_country_code(iban):
    iban_code = iban.upper().replace(' ', '').replace('-', '')
    country_code = iban_code[:2]
    if country_code in IBAN_COUNTRY_CODE_LENGTH or country_code in NORDEA_COUNTRY_CODE_LENGTH:
        return country_code
    return None
