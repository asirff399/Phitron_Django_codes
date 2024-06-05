from django.shortcuts import render,redirect
from musician.forms import MusicianForm
# Create your views here.
def musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm()
    return render(request,'musician.html',{'form':form}) 