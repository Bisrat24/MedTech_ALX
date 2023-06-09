from django import forms
from drugs.models import Drugs


class DrugsForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = ('name', 'price', 'expiry_date')
