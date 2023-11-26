"""Models"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField

class Book(models.Model):
    """
    Model for Book
    
    The 'status' field represents the availability of the book:
    - 'a' stands for "Available" in the database.
    - 'b' stands for "Borrowed" in the database.
    
    Meta:
    To display the books in alphabetical order by title.
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
            ("Available", "a"),
            ("Borrowed", "b")
        ], default="Available"
    )
    return_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    
    class Meta:
        ordering = ['title']
        
        
    def get_absolute_url(self):
        """Get URL for book detail view."""
        return reverse('book:book_detail', kwargs={'slug': self.slug})
        
        
    def __str__(self):
        return f"{self.title}"