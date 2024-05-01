# forms.py
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'age', 'username', 'password', 'cpassword']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'cpassword': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your cpassword'}),
            
        }
