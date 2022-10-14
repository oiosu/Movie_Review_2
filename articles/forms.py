from django import forms
from .models import Review

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade']