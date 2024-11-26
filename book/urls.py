from django.urls import path
from rest_framework.routers import DefaultRouter

from book.apps import BookConfig
from book.views import BookViewSet

app_name = BookConfig.name

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="books")
urlpatterns = [
    # path('list_books/', BookViewSet.as_view({'get': 'list_books'}), name='list_books'),
    # path('list_books/', BookViewSet.as_view({'get': 'list_books'}), name='list_books'),
] + router.urls

