from django import forms
from .models import Article, Comment


class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = ['title', 'body', 'category', 'author']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class EmailForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField()
