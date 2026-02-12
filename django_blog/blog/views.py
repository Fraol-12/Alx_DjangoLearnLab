from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserUpdateForm, PostForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post 
from django.urls import reverse_lazy 


def home(request):
    return render(request, 'blog/base.html')

def post_list(request):
    return HttpResponse("post list page")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect('login')
        
    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html', {'form':form})       

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfuly!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)    

    return render(request, 'blog/profile.html', {'form': form})    

# View single post
class PostListView(ListView):
    model = Post 
    template_name = 'blog/post_list.html'
    context_object_name = 'post' 
# View single post

class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html' 
    context_object_name = 'post' 

# Create a post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm  
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 
    
# update a post    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    form_class = PostForm 
    template_name = 'blog/post_form.html' 

    def test_func(self):
        post = self.get_object() 
        return self.request.user == post.author 
    
# Delete a post 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    template_name = 'blog/post_confirm_delete.html' 
    success_url = reverse_lazy('posts') 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author     



