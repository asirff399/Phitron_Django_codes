from django import forms
from . import models
class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = "__all__"
        # fields = ['name','roll']
        # exclude = ['roll']
        labels = {
            'name':'Student Name',
            'roll':'Student Roll'
        }
        # widgets={
        #     'name': forms.TextInput(attrs={'class':"bg-dark text-light"})
        # }  
        help_texts = {
            'name':'Enter your full name'
        }
        error_massages = {
            'name':{'required':'Your name is required'} 
        } 