import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from books.models import Author, Book
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username="user1", email="user1@example.com", password="password123")

@pytest.fixture
def another_user():
    return User.objects.create_user(username="user2", email="user2@example.com", password="password123")

@pytest.fixture
def token_client(user, api_client):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.mark.django_db
def test_create_book(token_client, user):
    url = reverse("book-list")
    payload = {
        "title": "The Hobbit",
        "authors": [{"name": "J.R.R. Tolkien"}],
        "genre": "Fantasy",
        "publication_date": str(date.today()),
        "description": "Adventure story"
    }
    response = token_client.post(url, payload, format="json")
    print(response.status_code)
    print(response.data)
    assert response.status_code == 201
    assert response.data["book"]["title"] == "The Hobbit"

@pytest.mark.django_db
def test_get_books_public(api_client):
    url = reverse("book-list")
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_book_only_by_creator(token_client, another_user):
    book = Book.objects.create(
        title="To Update",
        genre="Sci-Fi",
        publication_date=date.today(),
        created_by=another_user
    )
    url = reverse("book-detail", kwargs={"pk": book.id})
    response = token_client.put(url, {
        "title": "Updated Title",
        "authors": [{"name": "Anon"}],
        "genre": "Sci-Fi",
        "publication_date": str(date.today()),
        "description": "Updated"
    }, format="json")
    assert response.status_code == 403

@pytest.mark.django_db
def test_delete_book_only_by_creator(token_client, another_user):
    book = Book.objects.create(
        title="To Delete",
        genre="Drama",
        publication_date=date.today(),
        created_by=another_user
    )
    url = reverse("book-detail", kwargs={"pk": book.id})
    response = token_client.delete(url)
    assert response.status_code == 403
