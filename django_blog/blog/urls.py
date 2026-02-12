from django.urls import path
from django.http import HttpResponse
from . import views
from django.contrib.auth import views as auth_views


def home(request):
    return HttpResponse("Blog Home Page")

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.post_list, name='posts'),
]
