from django.forms import ModelForm, Textarea
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {     
            'username' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['user', 'inflow', 'outflow']

        widgets = {
            'name' : forms.TextInput(),
            'cin' : forms.TextInput(),
            'address': forms.Textarea(),
            'classification': forms.Select(),
            'industry' : forms.TextInput(),
            'revenue' : forms.NumberInput(),
        }

class InflowProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['type', 'value']

        widgets = {
            'name' : forms.TextInput(),
            'description' : forms.Textarea(),
            'unit' : forms.Select(),
        }

class OutflowProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['type']

        widgets = {
            'name' : forms.TextInput(),
            'description' : forms.Textarea(),
            'value' : forms.NumberInput(),
            'unit' : forms.Select(),
        }