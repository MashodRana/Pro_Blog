from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    """ Form for user creation """
    password1 = forms.CharField(label='Password', widget=(forms.PasswordInput(attrs={'class':'form-control'})))
    password2 = forms.CharField(label='Password Confirmation', widget=(forms.PasswordInput(attrs={'class':'form-control'})))

    class Meta:
        model = CustomUserModel
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),

        }


class CustomUserChangeForm(UserChangeForm):
    """ Form for changing user information """

    class Meta:
        model = CustomUserModel
        fields = ('email', 'age', 'profession', 'first_name', 'last_name', )
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'profession': forms.TextInput(attrs={'class':'form-control'}),
        }


class CustomLoginForm(AuthenticationForm):
    """ Form for Log into the Blog """
    
    password = forms.CharField(widget=(forms.PasswordInput(attrs={'class':'form-control'})))
    username = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control'})))

    class Meta:
        Model = CustomUserModel
        fields = ('username', 'password')



