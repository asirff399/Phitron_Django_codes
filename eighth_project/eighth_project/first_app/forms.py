from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'requared'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'requared'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id':'requared'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']   

class ChangeUserDataForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']  