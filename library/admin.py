"""imports for admin page"""

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Allows admin to manage books via the admin panel"""
    list_filter = ('title', 'status')
    list_display = ('title', 'slug', 'status')
    search_fields = ('title', 'description')