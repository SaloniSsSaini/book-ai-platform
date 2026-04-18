# backend/config/urls.py

from django.contrib import admin
from django.urls import path

from apps.books.views import list_books, book_detail
from apps.rag.views import ask

urlpatterns = [
    path('admin/', admin.site.urls),

    # Books APIs
    path('api/books/', list_books),
    path('api/books/<int:pk>/', book_detail),

    # RAG API
    path('api/ask/', ask),
]