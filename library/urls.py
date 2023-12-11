"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('my_books/', views.MyBooks.as_view(), name='my_books'),
    path('edit_book/<slug:slug>/', views.EditBook.as_view(), name='edit_book'),
    path('delete_book/<slug:slug>/', views.DeleteBook.as_view(), name='delete_book'),
]