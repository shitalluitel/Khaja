from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(
        label="Company Name",
        widget = forms.TextInput(attrs={"class":"form-control"}),
    )

    location = forms.CharField(
        label="Address",
        widget = forms.TextInput(attrs={"class":"form-control"}),
    )

    phone_no = forms.CharField(
        label = "Phone no.",
        widget = forms.TextInput(attrs={"class":"form-control"}),
    )

    class Meta:
        model = Company
        fields = [
        'company_name',
        'location',
        'phone_no',
        ]
