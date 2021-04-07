from django import forms
from .models import Artist, Album
class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ('name', 'bio')

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = ('artist', 'year', 'title')