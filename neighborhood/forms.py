from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# registering user
class Registration(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']


    # user post class