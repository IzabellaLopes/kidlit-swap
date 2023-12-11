"""Forms for Books"""

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """ Create Book Form """
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