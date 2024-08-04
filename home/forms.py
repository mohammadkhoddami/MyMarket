from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'stars', )
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form__input form__input--textarea', 'id': 'review'}),
            'stars': forms.Select(attrs={'class': 'form__input', 'id': 'stars'}, choices=Comment.STARS_CHOICE),
        }