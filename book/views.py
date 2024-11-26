from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from book.models import Book
from book.paginators import Pagination
from book.permissions import IsUserModerator
from book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()
