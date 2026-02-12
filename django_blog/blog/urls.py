from django.urls import path
from django.http import HttpResponse
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostCreateView, PostDeleteView,
    PostListView, PostDetailView, PostUpdateView
)



def home(request):
    return HttpResponse("Blog Home Page")

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]



  