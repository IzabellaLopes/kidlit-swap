"""Views"""

from django.shortcuts import render
from django.views import generic
from .models import Book


class BookList(generic.ListView):
    """
    View to display a paginated list of books in alphabetical order
    """
    model = Book
    template_name = 'books_list.html'
    paginate_by = 8
    
    def get_queryset(self):
        """
        Retrieve the queryset of books, 
        ordered alphabetically with available books first
        """
        return Book.objects.order_by('status', 'title')

    def get_context_data(self, **kwargs):
        """
        Add additional context data for available and borrowed book counts
        """
        context = super().get_context_data(**kwargs)
        context['available_count'] = Book.objects.filter(status='a').count()
        context['borrowed_count'] = Book.objects.filter(status='b').count()
        return context