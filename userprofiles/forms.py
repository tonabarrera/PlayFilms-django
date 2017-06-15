from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailField

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


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['required'] = 'required'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        for visible in self.fields:
            self.fields[visible].widget.attrs['class'] = 'form-control'



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for visible in self.fields:
            self.fields[visible].widget.attrs['class'] = 'form-control-file'


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['number', 'owner', 'due_month', 'due_year', 'CVV']

    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)
        for visible in self.fields:
            self.fields[visible].widget.attrs['class'] = 'form-control'
