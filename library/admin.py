"""imports for admin page"""

from django.contrib import admin
from .models import Book, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Allows admin to manage categories via the admin panel"""
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Allows admin to manage books via the admin panel"""
    list_filter = ('title', 'status')
    list_display = (
        'title',
        'slug',
        'author',
        'status',
        'return_date',
        'added_by'
    )
    search_fields = ('title', 'author')
