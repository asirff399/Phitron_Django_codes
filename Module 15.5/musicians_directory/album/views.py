from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import Album
# Create your views here.
def album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(request,'album.html',{'form':form})

def edit_data(request,id):
    album = Album.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm(instance=album)
    return render(request,'album.html',{'form':form})


def delete_data(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')