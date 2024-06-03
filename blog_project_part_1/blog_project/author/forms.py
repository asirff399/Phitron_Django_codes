from django import forms
from . import models

class AuthorFrom(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'