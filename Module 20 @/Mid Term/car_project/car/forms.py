from django import forms
from . import models

class CarForm(forms.ModelForm):
    class Meta:
        model = models.Cars
        # fields = '__all__'
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body'] 

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['quantity']  