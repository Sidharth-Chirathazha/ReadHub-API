from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    authors = models.ManyToManyField(Author, related_name="books")
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def save(self, *args, **kwargs):
        """Ensure title is stored in Title Case before saving."""
        self.title = self.title.title()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
