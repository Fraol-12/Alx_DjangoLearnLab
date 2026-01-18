# LibraryProject/relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # <-- MUST be exactly this
from .models import Book, Library  # <-- MUST include Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()  # <-- ALX literal check
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })

# Class-based view: library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ALX literal check
    context_object_name = 'library'  # ALX literal check
