from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from book_api.models import Book
from book_api.serializer import BookSerializer
# Create your views here.

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serialazier= BookSerializer(books,many=True)
    return Response(serialazier.data)

@api_view(["GET"])
def book_details(request,id):
    try:
        book =Book.objects.get(pk=id)
        serializer= BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response({
            "error":"Model Bulunamadı"
        },status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error_messages)
@api_view(["PUT"])
def book_update(request,id):
    book =Book.objects.get(pk=id)
    serializer = BookSerializer(book,data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error_messages)

@api_view(["DELETE"])
def book_delete(request,id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response({"response":True})