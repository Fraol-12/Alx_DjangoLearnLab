from django import forms 
from django.contrib.auth.models import User 
from .models import Post , Comment


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']        

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True
    )

    class Meta:
        model = Comment
        fields = ['content']
  