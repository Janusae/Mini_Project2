from django import forms
from django.core.exceptions import ValidationError

from . import views
class Form_Register(forms.Form):
    username = forms.CharField(label="نام کاربری")
    email = forms.EmailField(label="ایمیل" , widget=forms.EmailInput())
    password = forms.CharField(label="گذرواژه" , widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="تکرار گذرواژه" , widget=forms.PasswordInput())
    def clean_confirm_password(self):
        passwd = self.cleaned_data.get("password")
        C_passwd = self.cleaned_data.get("confirm_password")
        if passwd == C_passwd:
            return C_passwd
        else:
            return ValidationError(passwd , "Your passwd and your confirm passwd is not the same")