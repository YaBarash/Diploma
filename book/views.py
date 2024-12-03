from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from book.models import Book, Author, Genre, BookItem
from book.paginators import Pagination
from book.permissions import IsUserModerator, IsUserOwner
from book.serializers import BookSerializer, AuthorSerializer, GenreSerializer, BookItemSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "authors__full_name", "genre__title"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Book.objects.filter(bookitem__gt=0)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator, IsAdminUser)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser)
        return super().get_permissions()

    """   
    Отслеживание статуса книги (когда выдана, кому, когда отдать)
    Уменьшать счетчик по количеству свободных книг
    Docker и ReadMe
    OpenAPI
    Возможно переписать на джанге, чтобы была верстка?
     """


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = Pagination

    def create(self, request, *args, **kwargs):
        lower_title = request.data["title"].lower()
        try:
            genre = Genre.objects.create(title=lower_title)
            return HttpResponse(genre)
        except:
            data = {
                "error": f"Ошибка с кодом 400. Объект с названием {lower_title} уже существует"
            }
            return JsonResponse(
                data["error"],
                safe=False,
                status=status.HTTP_400_BAD_REQUEST,
                json_dumps_params={"ensure_ascii": False},
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        return super().get_permissions()


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = Pagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        return super().get_permissions()


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    pagination_class = Pagination

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsUserOwner | IsUserModerator)
        return super().get_permissions()
