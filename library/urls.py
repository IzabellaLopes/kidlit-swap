"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]