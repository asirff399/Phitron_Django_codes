from django.shortcuts import render,redirect
from django.contrib import messages
from . import forms
# Create your views here.
def add_brand(request):
    if request.method == 'POST':
        form = forms.Brand(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Brand added successfully.')
            return redirect('add_brand')
    else:
        form = forms.Brand()
        return render(request,'add_brand.html',{'form': form})