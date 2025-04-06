from rest_framework import serializers
from .models import ReadingListItem, ReadingList
from books.models import Book
from base.validators import text_validator

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title"]

class ReadingListItemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = ReadingListItem
        fields = ["id", "book", "order"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["book"] = BookSerializer(instance.book).data
        return rep

class ReadingListSerializer(serializers.ModelSerializer):
    items = ReadingListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingList
        fields = ["id", "title", "description", "created_at", "items"]

class ReadingListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = ['id', 'title', 'description']

    def validate_title(self, value):
        text_validator(value, field="title")
        return value
    
    def validate_description(self, value):
        text_validator(value, field="Description")
        return value