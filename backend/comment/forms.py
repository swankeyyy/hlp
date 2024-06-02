from django import forms
from .models import Comment


class NewCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'comment_content',
                                     'placeholder': ' Оставьте ваш комментарий...', 'style': "height: 100px"}))

    class Meta:
        model = Comment
        fields = ['content']
