from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        try:
            if not self.request.user.is_authenticated:
                raise NotAuthenticated(detail="You must be logged in to add a book.")
            book = serializer.save(created_by=self.request.user)
            return Response(
                {
                    "message": "Book added successfully!",
                    "book": BookSerializer(book).data, 
                },
                status=status.HTTP_201_CREATED,
             )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        try:
            book = self.get_object()
            if book.created_by != request.user:
                raise PermissionDenied(detail="You do not have permission to edit this book.")
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            if instance.created_by != request.user:
                raise PermissionDenied(detail="You do not have permission to delete this book.")
            instance.delete()
            return Response({"message": "Book deleted successfully!"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied as e:
            return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       