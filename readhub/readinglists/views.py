from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import ReadingListItem, ReadingList
from .serializers import ReadingListCreateSerializer, ReadingListItemSerializer, ReadingListSerializer

# Create your views here.


class ReadingListViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ReadingList.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return ReadingListCreateSerializer
        return ReadingListSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddBookToReadingList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, reading_list_id):
        try:
            reading_list = ReadingList.objects.get(id=reading_list_id, user=request.user)
        except ReadingList.DoesNotExist:
            return Response({'detail': 'Reading list not found'}, status=404)
        
        serializer = ReadingListItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reading_list=reading_list)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class RemoveBookFromReadingList(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, reading_list_id, item_id):
        try:
            item = ReadingListItem.objects.get(id=item_id, reading_list__id = reading_list_id, reading_list__user=request.user)
            item.delete()
            return Response({'detail': 'Book removed from reading list'}, status=204)
        except ReadingListItem.DoesNotExist:
            return Response({'detail': 'Item not found'}, status=404)


