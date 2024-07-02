from django import forms
from . import models

class CategoryFrom(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'