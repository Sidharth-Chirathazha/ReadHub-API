import pytest
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

@pytest.mark.django_db
def test_author_serializer_create():
    serializer = AuthorSerializer(data={"name": "George Orwell"})
    assert serializer.is_valid()
    author = serializer.save()
    assert author.name == "George Orwell"

@pytest.mark.django_db
def test_book_serializer_create():
    user = User.objects.create_user(username="user", email="user@example.com", password="pass")
    data = {
        "title": "1984",
        "authors": [{"name": "George Orwell"}],
        "genre": "Dystopian",
        "publication_date": str(date.today()),
        "description": "A dystopian novel.",
    }

    serializer = BookSerializer(data=data)
    serializer.context["request"] = None  # fake context to avoid missing
    assert serializer.is_valid(), serializer.errors
    book = serializer.save(created_by=user)

    assert book.title == "1984"
    assert book.genre == "Dystopian"
    assert book.created_by == user
    assert book.authors.first().name == "George Orwell"
