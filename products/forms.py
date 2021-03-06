from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
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
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something about this food.', 'rows': 2}),
    )

    image = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(attrs={'class':'form-control-file product-image-btn'}),
    )

    time = forms.IntegerField(
        label="Time to Prepare",
        widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '120'})
    )

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'description',
            'time',
            'image',
        ]


class ProductEditForm(forms.ModelForm):
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
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something about this food.', 'rows': 2}),
    )

    image = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(),
        required=False,
    )
    time = forms.IntegerField(
        label="Time to Prepare",
        widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '120'})
    )

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'description',
            'image',
            'time',
        ]
