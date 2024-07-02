from django import forms
from . import models

class PostFrom(forms.ModelForm):
    class Meta:
        model = models.Post
        # fields = '__all__'
        exclude = ['author'] 

class CommentFrom(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email','body']

        