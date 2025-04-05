from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReadingListViewSet, AddBookToReadingList, RemoveBookFromReadingList

router = DefaultRouter()
router.register(r'reading-lists', ReadingListViewSet, basename="readinglists")

urlpatterns = [
    path('', include(router.urls)),
    path('reading-lists/<int:reading_list_id>/add-book/', AddBookToReadingList.as_view(), name='add-book'),
    path('reading-lists/<int:reading_list_id>/remove-book/<int:item_id>/', RemoveBookFromReadingList.as_view(), name='remove-book'),
]