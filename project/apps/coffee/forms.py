from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Coffee, Feedback


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    first_name = forms.CharField(label='Firstname', widget=forms.TextInput(attrs={'class': 'form-input'})),
    last_name = forms.CharField(label='Lastname', widget=forms.TextInput(attrs={'class': 'form-input'})),
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'})),
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    password2 = forms.CharField(label='RPassword', widget=forms.PasswordInput(attrs={'class': 'form-input'})),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'})),
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'})),

    class Meta:
        model = User
        fields = ('usernamr', 'password')


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = '__all__'

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


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'rating']

        widgets = {
            "text": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "rating": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'rating'
            })
        }
