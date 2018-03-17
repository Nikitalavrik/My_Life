from django import forms
from music import models

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = ("name","url","user")