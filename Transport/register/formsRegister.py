from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class registerForm(forms.Form):
    firstname = forms.CharField(
                           max_length=50,
                           label="First Name:"
                          )
    lastname = forms.CharField(
                           max_length=50,
                           label="Last Name:"
                          )
    email = forms.EmailField(
                             max_length=90,
                             widget=forms.TextInput(attrs={"type": "email"}), 
                             label="E-mail:"
                            )
    confirmemail = forms.EmailField(
                             max_length=90,
                             widget=forms.TextInput(attrs={"type": "email"}), 
                             label="Confirm E-mail:"
                            )
    phone = forms.CharField(
                            widget=forms.TextInput(attrs={"type": "tel", "maxlength": "14", "onkeyup": "handlePhone(event)"}),
                            required=False,
                            label="Phone:"
                           )
    password = forms.CharField(
                            widget=forms.TextInput(attrs={"type": "password"}),
                            label="Password with 6 digits"
                           )
    passwordconfirm = forms.CharField(
                            widget=forms.TextInput(attrs={"type": "password"}),
                            label="Confirm Password"
                           )
    

