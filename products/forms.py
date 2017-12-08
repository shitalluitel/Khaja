from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MoMo'}),
    )

    product_price = forms.DecimalField(
        label="Price",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '6', 'min': '0'})
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something about this food.'}),
    )

    image = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(),
    )

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'description',
            'image',
        ]
