from django import forms

class contactUsForm(forms.Form):
    name = forms.CharField(
                           max_length=50,
                           label="Name:"
                          )
    email = forms.EmailField(
                             max_length=90,
                             widget=forms.TextInput(attrs={"type": "email"}), 
                             label="E-mail:"
                            )
    phone = forms.CharField(
                            widget=forms.TextInput(attrs={"type": "tel", "maxlength": "14", "onkeyup": "handlePhone(event)"}),
                            required=False,
                            label="Phone:"
                           )
    ticket = forms.CharField(
                             max_length=25,
                             required=False, 
                             label="Ticket:"
                            )
    message = forms.CharField(
                              max_length=1000,
                              widget=forms.Textarea,
                              label="Speak your mind, please:"
                             )