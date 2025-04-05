from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book


User = get_user_model()

class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reading_lists")
    title = models.TextField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
class ReadingListItem(models.Model):
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ("reading_list", "book")
        ordering = ["order"]

    def __str__(self):
        return f"{self.book.title} in {self.reading_list.title} at position {self.order}"
