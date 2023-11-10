from django import forms

class contactUsForm(forms.Form):
    name = forms.CharField(max_length=50, 
                           widget=forms.TextInput(attrs={"class": "form-control"}), 
                           label="Name:"
                          )
    email = forms.EmailField(widget=forms.TextInput(attrs={"type": "email"}), 
                             label="E-mail:"
                            )
    phone = forms.CharField(max_length=13, 
                            widget=forms.NumberInput(attrs={"type": "number"}), 
                            label="Phone:"
                           )