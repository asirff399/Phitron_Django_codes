from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile_froms = forms.ProfileFrom(request.POST)
        if profile_froms.is_valid():
            profile_froms.save()
            return redirect('add_author')
    else:
        profile_froms = forms.ProfileFrom()
    return render(request,'add_profile.html',{'form':profile_froms})    