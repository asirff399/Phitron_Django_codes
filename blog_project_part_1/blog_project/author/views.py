from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_author(request): 
    if request.method == 'POST':
        author_froms = forms.AuthorFrom(request.POST)
        if author_froms.is_valid():
            author_froms.save()
            return redirect('add_author')
    else:
        author_froms = forms.AuthorFrom()
    return render(request,'add_author.html',{'form':author_froms})   