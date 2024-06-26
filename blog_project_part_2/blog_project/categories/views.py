from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request): 
    if request.method == 'POST':
        category_froms = forms.CategoryFrom(request.POST)
        if category_froms.is_valid():
            category_froms.save()
            return redirect('add_categories')
    else:
        category_froms = forms.CategoryFrom()
    return render(request,'add_author.html',{'form':category_froms})