from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # <-- MUST include Library


def list_books(request):
    books = Book.objects.all()  # <-- MUST be exactly this
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # <-- MUST match this exactly
    context_object_name = 'library' 