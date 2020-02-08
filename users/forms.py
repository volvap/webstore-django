from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]
