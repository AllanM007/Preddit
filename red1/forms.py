from django.forms import ModelForm, Select, Textarea
from django import forms
from .models import LoggedInUser, Subweddit, Post, Comment

SUB_WEDDITS=(
    ('w/tech','w/tech'),
    ('w/memes','w/memes'),
    ('w/cars','w/cars'),
    ('w/movies','w/movies'),
    )

class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()

class PostForm(forms.ModelForm):
    weddits = forms.ModelMultipleChoiceField(queryset=Subweddit.objects.all())
    #weddits = forms.ChoiceField(choices=SUB_WEDDITS)


    class Meta:
        model = Post
        fields = ['weddits', 'body']
        widgets = {
            'body': Textarea(attrs={'cols': 8, 'rows': 4}),
            #'weddits': Select(attrs={'class': 'form-control'})
            'weddits': forms.Select()
        }

    field_order = ['weddits', 'body', 'author']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']