from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    """Render book in list view"""
    model = Book
    template_name = 'book_list.html'
