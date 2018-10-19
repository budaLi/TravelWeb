# @Time    : 18-10-11
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

from django import forms
from captcha.fields import CaptchaField

from .models import *


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={'invalid': '验证码有误'})


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码有误'})


class NewPwdForm(forms.Form):
    pwd1 = forms.CharField(required=True, min_length=8)
    pwd2 = forms.CharField(required=True, min_length=8)


class InfoForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['nickname', 'gender', 'city_addr', 'birthday', 'signature']