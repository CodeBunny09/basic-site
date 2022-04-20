from django.contrib.auth.forms import UserCreationForm
from account.models import User, UserMeta
from django.forms import ModelForm
from django import forms

# Widget for forms
class DateInput(forms.DateInput):
    input_type = 'date'

# Forms
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

class UserMetaForm(ModelForm):
    birthday = forms.DateField(widget=DateInput)
    class Meta:
        model = UserMeta
        fields = ['birthday', 'works_for']
