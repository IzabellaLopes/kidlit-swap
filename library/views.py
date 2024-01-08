"""Views"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Book, Category
from .forms import BookForm, BookBorrowForm


class Home(generic.TemplateView):
    """
    View to display the home page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        Discover Our Features
        """
        features = [
            {
                "icon": "book",
                "title": "Explore Our Library",
                "description1": ("Find books for kids and add your favorites "
                                 "to our collection"),
                "description2": ("Be part of our growing community of young "
                                 "readers"),
            },
            {
                "icon": "book-open-reader",
                "title": "See What's Available and Borrow",
                "description1": "Check which books are ready to borrow",
                "description2": ("Pick a date that works for you to enjoy "
                                 "a smooth borrowing process"),
            },
            {
                "icon": "child-reaching",
                "title": "Enjoy Quality Time with Your Kids",
                "description1": "Have fun reading with your children",
                "description2": ("Create wonderful memories with enchanting "
                                 "stories"),
            },
        ]

        context = super().get_context_data(**kwargs)
        context['features'] = features
        return context


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
        context['categories'] = Category.objects.all()
        return context


class CategoryBookList(generic.ListView):
    """
    View to display a paginated list of books
    in alphabetical order based on category
    """
    template_name = 'category_books.html'
    paginate_by = 8

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        category = get_object_or_404(Category, name=category_name)
        return Book.objects.filter(category=category).order_by(
            'status', 'title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs.get('category_name')
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


class NewCategoryMixin:
    """
    Mixin to handle the creation of a new category
    when adding or editing a book
    """
    def form_valid(self, form):
        form.instance.added_by = self.request.user

        # Check if the user entered a new category
        new_category = form.cleaned_data.get('new_category', '').strip()
        if new_category:
            # Create a new Category instance
            category = Category.objects.create(
                name=new_category, description='')
            form.instance.category = category
        else:
            # Use the existing category selected in the form
            form.instance.category = form.cleaned_data.get('category')

        return super().form_valid(form)


class AddBook(
    NewCategoryMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.CreateView
):
    """
    View to allow logged in users to add a book
    """
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        return self.request.user.is_authenticated


class MyBooks(LoginRequiredMixin, generic.ListView):
    """
    View to display a list of books added by the logged-in user
    """
    model = Book
    template_name = 'my_books.html'
    context_object_name = 'user_books'

    def get_queryset(self):
        # Retrieve books added by the logged-in user
        return Book.objects.filter(added_by=self.request.user)


class BorrowedBooks(generic.ListView):
    """
    View to display a list of books borrowed by the logged-in user
    """
    model = Book
    template_name = 'borrowed_books.html'
    context_object_name = 'borrowed_books'

    def get_queryset(self):
        # Retrieve books borrowed by the logged-in user
        return Book.objects.filter(
            borrower=self.request.user,
            status='Borrowed'
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EditBook(
    NewCategoryMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    """
    View to edit a book added by the logged-in user
    """
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('my_books')

    def test_func(self):
        return self.request.user == self.get_object().added_by

    def form_valid(self, form):
        messages.success(self.request, 'Book successfully updated.')
        return super().form_valid(form)


class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    View for deleting a book
    """
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('my_books')

    def test_func(self):
        return self.request.user == self.get_object().added_by

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        if not book.can_delete():
            messages.error(
                self.request,
                f'You cannot delete this book because it is borrowed to '
                f'{book.borrower.username}'
            )
            return redirect('my_books')
        return super().get(request, *args, **kwargs)

# Date validation


def is_return_date_valid(selected_return_date):
    current_date = datetime.now().date()

    if selected_return_date and selected_return_date <= current_date:
        return False
    return True


class BorrowBookView(LoginRequiredMixin, View):
    """
    View to handle the borrowing of a book
    """
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)

        # Check if the book is available
        if book.status == 'Available':
            form = BookBorrowForm()
            return render(
                request,
                'book_detail.html',
                {'book': book, 'form': form, 'modal_open': True}
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
                    request, (
                        f'You have successfully borrowed the book '
                        f'"{book.title.upper()}"'
                    )
                )

                return redirect('book_detail', slug=slug)
            else:
                messages.error(
                    request, 'Invalid form data. Please try again.'
                    )
                return render(
                    request, 'book_detail.html', {'book': book, 'form': form}
                    )
        else:
            messages.error(
                request, 'This book is not available for borrowing.'
                )
            return redirect('book_detail', slug=slug)


class ReturnBookView(LoginRequiredMixin, View):
    """
    View to handle the return of a borrowed book
    """
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)

        # Check if the book is borrowed by the logged-in user
        if book.status == 'Borrowed' and book.borrower == request.user:
            book.status = 'Available'
            book.borrower = None
            book.return_date = None
            book.save()

            messages.success(
                request, (
                    f'You have successfully returned the book '
                    f'"{book.title.upper()}"'
                    )
            )

        else:
            messages.error(request, 'This book cannot be returned.')

        return redirect('borrowed_books')


class CustomSignupView(SignupView):
    """
    Sign up form validation and displaying error messages

    Methods:
        form_invalid(form): Handles form submission when the form is invalid.
    """
    def form_invalid(self, form):
        """
        Handle form submission when the form is invalid

        Args:
            form (django.forms.Form): The invalid form submitted by the user

        Returns:
            django.http.HttpResponse:
            The response generated by the superclass method
        """
        response = super().form_invalid(form)

        # Collect all error messages
        error_messages = []

        # Collect password-related error messages
        password_errors = form.errors.get('password1', [])
        for error in password_errors:
            if 'at least 8 characters' in error:
                error_messages.append(
                    'This password is too short. '
                    'It must contain at least 8 characters.'
                )
            elif 'too common' in error:
                error_messages.append(
                    'This password is too common. Try another one.'
                )
            elif 'numeric' in error:
                error_messages.append('This password is entirely numeric.')

        # Check if passwords do not match
        if (
            form.cleaned_data.get('password1')
            !=
            form.cleaned_data.get('password2')
        ):
            error_messages.append('Passwords do not match.')

        # Check for existing username or blank/whitespace
        if (
            not form.cleaned_data.get('username') or
            form.cleaned_data.get('username').isspace()
        ):
            error_messages.append(
                'Username error: '
                'Check availability and avoid blank or whitespace characters.'
            )

        # Display all error messages
        for error_message in error_messages:
            messages.error(self.request, error_message)

        return response


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """
    View to display the user profile page
    """
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve books added by the logged-in user and count
        user_books = Book.objects.filter(added_by=self.request.user)
        books_added_count = user_books.count()

        # Add the count to the context
        context['books_added_count'] = books_added_count

        return context
