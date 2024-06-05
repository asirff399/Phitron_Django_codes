from django import forms
from album.models import Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': ('Album Name'),
            'release_date': ('Release Date'),
            'rating': ('Rate Here'),
        }
        widgets = {
            'rating': forms.RadioSelect()   
        }

