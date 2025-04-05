import pytest
from books.models import Author, Book
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

@pytest.mark.django_db
def test_author_str_and_save():
    author = Author.objects.create(name="  jane austen ")
    assert author.name == "Jane Austen"
    assert str(author) == "Jane Austen"

@pytest.mark.django_db
def test_book_str_and_save():
    user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass123")
    book = Book.objects.create(
        title="pride and prejudice",
        genre="Fiction",
        publication_date=date.today(),
        created_by=user
    )
    assert book.title == "Pride And Prejudice"
    assert str(book) == "Pride And Prejudice"
