from django import forms
from django.forms import Textarea
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'country', 'state', 'postal_code']
        widgets = {
            'address_line_1': Textarea(attrs={'class': 'form-control'}),
            'address_line_2': Textarea(attrs={'class': 'form-control'}),
            'city': Textarea(attrs={'class': 'form-control'}),
            'country': Textarea(attrs={'class': 'form-control'}),
            'state': Textarea(attrs={'class': 'form-control'}),
            'postal_code': Textarea(attrs={'class': 'form-control'}),
        }
