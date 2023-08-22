from django import forms

from .models import Coffee


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['title', 'description', 'info', 'price', 'pictures']

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name coffee'
            }),
            "description": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "info": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Info'
            }),
            "price": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            "pictures": forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
