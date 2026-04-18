from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()
    return Response(BookSerializer(books, many=True).data)

@api_view(['GET'])
def book_detail(request, id):
    book = Book.objects.get(id=id)
    return Response(BookSerializer(book).data)