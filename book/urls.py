from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.apps import BookConfig
from book.views import BookViewSet, AuthorViewSet, GenreViewSet, BookItemViewSet

app_name = BookConfig.name

router1 = DefaultRouter()
router1.register(r"books", BookViewSet, basename="books")
router2 = DefaultRouter()
router2.register(r"authors", AuthorViewSet, basename="authors")
router3 = DefaultRouter()
router3.register(r"genres", GenreViewSet, basename="genres")
router4 = DefaultRouter()
router4.register(r"book_details", BookItemViewSet, basename="book_details")
urlpatterns = [
    path("", include(router1.urls)),
    path("", include(router2.urls)),
    path("", include(router3.urls)),
    path("", include(router4.urls)),
]
