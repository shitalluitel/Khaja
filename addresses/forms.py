from django import forms
from django.forms import TextInput
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'country', 'state', 'phone_number']
        widgets = {
            'address_line_1': TextInput(attrs={'class': 'form-control'}),
            'address_line_2': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'class': 'form-control'}),
        }
