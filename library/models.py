"""Models"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model representing a category for organizing books

    Attributes:
        name (str): The name of the category.
        description (str): A brief description of the category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model for Book

    """
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.CharField(max_length=200)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", default=None
        )
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.CharField(
        max_length=10,
        choices=[
            ("Available", "Available"),
            ("Borrowed", "Borrowed")
        ], default="Available"
    )
    borrower = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="borrowed_books",
        null=True,
        blank=True
    )
    return_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="books", null=True)

    class Meta:
        """Display the books in alphabetical order by title"""
        ordering = ['title']

    def get_absolute_url(self):
        """Get URL for book detail view"""
        return reverse('book_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"