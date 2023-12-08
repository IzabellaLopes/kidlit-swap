"""Views"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Book


class Home(generic.TemplateView):
    """
    View to display the home page
    """
    template_name = "index.html"
    

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
        context['books'] = context['object_list']      
        return context    

class BookDetail(generic.DetailView):
    """
    View to display detailed information about a book
    """
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        """
        Get the book based on the slug
        """
        slug = self.kwargs.get('slug')
        return get_object_or_404(Book, slug=slug)
    

@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'profile.html'