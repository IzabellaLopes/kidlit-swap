"""Models"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Book(models.Model):
    """
    Model for Book

    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", default=None
        )
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    return_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )