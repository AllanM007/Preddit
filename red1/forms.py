from django.forms import ModelForm
from django import forms
from .models import LoggedInUser, Subweddit, Post, Comment

SUB_WEDDITS=(
    ('w/tech','w/tech'),
    ('w/memes','w/memes'),
    ('w/cars','w/cars'),
    ('w/movies','w/movies'),
    )

class PostForm(forms.ModelForm):
    weddits = forms.ChoiceField(choices=SUB_WEDDITS)

    class Meta:
        model = Post
        fields = ['body', 'author']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']