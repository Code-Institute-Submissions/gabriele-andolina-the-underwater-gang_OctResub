from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        content = SummernoteTextFormField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'content',)
        widgets = {
            'content': SummernoteWidget(),
        }

