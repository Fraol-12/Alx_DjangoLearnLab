from django import forms 
from django.contrib.auth.models import User 
from .models import Post , Comment, Tag


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='comma-separated tags')

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']        

    def save(self, commit=True):
        instance = super().save(commit=False)    

        if commit:
            instance.save()

        tags_data = self.cleaned_data['tags']    
        tag_list = [tag.strip() for tag in tags_data.spilt(',') if tag.strip()] 

        instance.tags.clear()
        
        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return instance    

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True
    )

    class Meta:
        model = Comment
        fields = ['content']
  