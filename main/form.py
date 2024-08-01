from django import forms
from django.contrib.auth.models import User

from main.models import Car



class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("Passwords don't match")
        else:
            return cd.get('password2')

    # password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput())

class NewLoginForm(forms.Form):
    username = forms.CharField(label='Логин')


class NewPasswordForm(forms.Form):
    password = forms.CharField(label='Логин')
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

