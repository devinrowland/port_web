from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))