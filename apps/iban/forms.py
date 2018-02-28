from django import forms
from django.core.exceptions import ValidationError

from .models import IBANAccount


class IBANAccountModelForm(forms.ModelForm):

    def clean_iban(self):
        """
        Check if IBAN already exist in IBANAccount model.
        :return: ValidationError or cleaned_data['iban']
        """
        iban = self.cleaned_data['iban']
        if self.instance._meta.default_manager.filter(iban=iban).exists():
            raise ValidationError('IBAN already exist')
        return iban

    class Meta:
        model = IBANAccount
        fields = ['first_name', 'last_name', 'iban', ]
