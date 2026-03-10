from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book

from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, pk):

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "No existe el libro"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        book.delete()
        return Response({"message": "Objeto eliminado"}, status=status.HTTP_204_NO_CONTENT)