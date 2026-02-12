from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog Home Page")

urlpatterns = [
    path('', home, name='home'),
]