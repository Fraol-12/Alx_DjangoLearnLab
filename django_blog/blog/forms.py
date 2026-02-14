from django import forms 
from django.contrib.auth.models import User 
from .models import Post , Comment, Tag
from taggit.forms import TagWidget

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Enter tags separated by commas'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        # handle tags
        tags_data = self.cleaned_data.get('tags', '')  # get tag string
        tag_list = [tag.strip() for tag in tags_data.split(',') if tag.strip()]

        instance.tags.clear()
        for tag_name in tag_list:
            instance.tags.add(tag_name)

        return instance   

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True
    )

    class Meta:
        model = Comment
        fields = ['content']
  