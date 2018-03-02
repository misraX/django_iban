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
        query_set = self.instance._meta.default_manager.filter(iban=iban)
        if self.instance.pk is not None:
            query_set = query_set.exclude(pk=self.instance.pk)
        if query_set.exists():
            raise ValidationError('IBAN already exist')
        return iban

    class Meta:
        model = IBANAccount
        fields = ['first_name', 'last_name', 'iban', ]
