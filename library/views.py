"""Views"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Book
from .forms import BookForm, BookBorrowForm


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
        context['available_count'] = (
            Book.objects.filter(status='available').count())
        context['borrowed_count'] = (
            Book.objects.filter(status='borrowed').count())
        context['books'] = context['object_list']
        context['form'] = BookForm()
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


class AddBook(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    """
    View to allow logged in users to add a book
    """
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated


class MyBooks(LoginRequiredMixin, generic.ListView):
    """
    View to display a list of books added and borrowed by the logged-in user
    """
    model = Book
    template_name = 'my_books.html'
    context_object_name = 'user_books'

    def get_queryset(self):
        # Retrieve books added by the logged-in user
        user_books = Book.objects.filter(added_by=self.request.user)

        # Retrieve books borrowed by the logged-in user
        borrowed_books = Book.objects.filter(borrower=self.request.user, status='Borrowed')

        # Combine the two querysets
        all_books = user_books | borrowed_books

        return all_books
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter borrowed books separately for display in the template
        borrowed_books = context['user_books'].filter(status='Borrowed')
        context['borrowed_books'] = borrowed_books

        return context

class EditBook(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('my_books')

    def test_func(self):
        return self.request.user == self.get_object().added_by


class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('my_books')

    def test_func(self):
        return self.request.user == self.get_object().added_by

# Date validation


def is_return_date_valid(selected_return_date):
    current_date = datetime.now().date()

    if selected_return_date and selected_return_date <= current_date:
        return False
    return True


class BorrowBookView(LoginRequiredMixin, View):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)

        # Check if the book is available
        if book.status == 'Available':
            form = BookBorrowForm()
            return render(
                request,
                'borrow_book.html',
                {'book': book, 'form': form}
            )
        else:
            messages.error(
                request,
                'This book is not available for borrowing.'
            )
            return redirect('book_detail', slug=slug)

    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)

        # Check if the book is available
        if book.status == 'Available':
            form = BookBorrowForm(request.POST)
            if form.is_valid():
                return_date = form.cleaned_data['return_date']

                # Use the utility function for date validation
                if is_return_date_valid(return_date):
                    # Update book status and borrower information
                    book.status = 'Borrowed'
                    book.borrower = request.user
                    book.return_date = return_date
                    book.save()

                messages.success(
                    request, f'You have successfully borrowed the book "{book.title}".'
                    )
                return redirect(
                    'book_detail', slug=slug
                    )
            else:
                messages.error(
                    request, 'Invalid form data. Please try again.'
                    )
                return render(
                    request, 'borrow_book.html', {'book': book, 'form': form}
                    )
        else:
            messages.error(
                request, 'This book is not available for borrowing.'
                )
            return redirect('book_detail', slug=slug)


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'profile.html'