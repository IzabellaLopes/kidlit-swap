"""Forms for Books"""

from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    Form for creating and editing a book

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        description (str): A description of the book.
        image (Image): The image associated with the book.
        category (Category): The category to which the book belongs.
    """

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image', 'category']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'description': 'Description',
            'image': 'Image',
            'category': 'Category',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class BookBorrowForm(forms.Form):
    """
    Form for handling the borrowing of a book

    Attributes:
        return_date (Date): The return date selected by the user.
    """
    return_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select the return date for the book.'
    )