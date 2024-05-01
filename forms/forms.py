from django import forms


class MyForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=100)
    lname = forms.CharField(label='Last Name', max_length=100)
    country = forms.CharField(label='Country', max_length=100)
    email = forms.CharField(label='Email')