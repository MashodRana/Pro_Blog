from django import forms

from .models import ArticleModel, CommentModel


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ('title', 'body',)
        labels = {'title':'Title', 'body':'Content'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='Write your comment.', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = CommentModel
        fields = ('comment',)


