from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from django.http.response import HttpResponse



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your password'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')

        if User.objects.filter(username=username).count() == 0:
            raise forms.ValidationError('The username entered is not linked to an account')
 
        return True

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you username'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter you email'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter you password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Renter you password'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you first name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you last name'}), required=True)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')


        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email entered is already registered.')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username entered is already in use.')

        if not len(password1) >= 8:
            raise forms.ValidationError('The password entred is less then 8 characters.')

        if not password1 == password2:
            raise forms.ValidationError("The passwords entered don't match.")
