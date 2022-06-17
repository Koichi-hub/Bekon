from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password repeat'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
