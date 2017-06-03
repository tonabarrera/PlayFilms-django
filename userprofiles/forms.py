from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput

from userprofiles.models import UserProfile, CreditCard

EXTRA_CHOICES = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput()
        }
        help_texts = {
            'username': ''
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            'password': 'Contraseña',
        }



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['number', 'owner', 'due_month', 'due_year', 'CVV']
