from django import forms
from django.forms import TextInput
from .models import Address


class AddressForm(forms.ModelForm):
    phone_number = forms.RegexField(regex=r'^\d{9,15}$',error_messages={'invalid': "Phone number must be entered in the format: '999999999'. Up to 15 digits allowed."})
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'country', 'state', 'phone_number']
        widgets = {
            'address_line_1': TextInput(attrs={'class': 'form-control'}),
            'address_line_2': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'class': 'form-control'}),
        }
