from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from book.models import Book, Author
from book.paginators import Pagination
from book.permissions import IsUserModerator
from book.serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        return super().get_permissions()

    def list(self):
        queryset = Book.objects.filter()


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = Pagination

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        return super().get_permissions()
