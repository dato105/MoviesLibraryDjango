from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['poster', 'title', 'description', 'director', 'four_main_actors', 'year_of_release']