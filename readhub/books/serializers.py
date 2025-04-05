from rest_framework import serializers
from .models import Book, Author
from base.validators import text_validator, author_validator, date_validator

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]

    def to_internal_value(self, data):
        name = data.get("name", "").strip()

        author = Author.objects.filter(name__iexact=name).first()
        if author:
            return {"id": author.id, "name": author.name}
        return super().to_internal_value(data)

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ["id", "title", "authors", "genre", "publication_date", "description"]

    def validate_title(self, value):
        text_validator(value, field="Title")
        
        formatted_title = value.title()

        if not self.instance or self.instance.title.lower() != formatted_title.lower():
            if Book.objects.filter(title__iexact=formatted_title).exists():
                raise serializers.ValidationError("A book with this title already exists.")
        return formatted_title
    
    def validate_authors(self, value):
        author_validator(value)
        return value

    def validate_genre(self, value):
        text_validator(value, field="Genre")
        return value
    
    def validate_description(self, value):
        text_validator(value, field="Description")
        return value
    
    def validate_publication_date(self, value):
        date_validator(value)
        return value

    def create(self, validated_data):
        authors_data = validated_data.pop("authors")
        book = Book.objects.create(**validated_data)

        for author_data in authors_data:
            author, created = Author.objects.get_or_create(name=author_data["name"])
            book.authors.add(author)
        
        return book
    
    def update(self, instance, validated_data):
        if "authors" in validated_data:
            authors_data = validated_data.pop("authors")
            instance.authors.clear()
            for author_data in authors_data:
                author,created = Author.objects.get_or_create(name=author_data["name"])
                instance.authors.add(author)

        return super().update(instance, validated_data)