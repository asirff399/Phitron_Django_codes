from django import forms
from models_app.models import TestModelForm

class TestModel(forms.ModelForm):
    class Meta:
        model = TestModelForm
        fields = "__all__" 
  