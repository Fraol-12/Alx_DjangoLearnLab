from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserUpdateForm


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