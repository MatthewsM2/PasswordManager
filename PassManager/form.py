from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Entry

from django.forms.widgets import PasswordInput, TextInput

# Registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2',]
        
# Authentication - Login
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# New Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['uid','title','uname','password','url','expire','notes',]
