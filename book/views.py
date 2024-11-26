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

    # def update(self, request):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.delete()
