from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book, Author, Genre, BookItem
from book.paginators import Pagination
from book.permissions import IsUserModerator, IsUserOwner
from book.serializers import (
    BookSerializer,
    AuthorSerializer,
    GenreSerializer,
    BookItemSerializer,
)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "authors__full_name", "genre__title"]

    # Автоматическое присвоение библиотекаря при создании книги
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Отображение списка книг, которые находятся в наличии
    def list(self, request, *args, **kwargs):
        if self.request.user == IsAdminUser or IsUserModerator:
            queryset = Book.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        if self.request.user == IsAuthenticatedOrReadOnly:
            queryset = Book.objects.filter(bookitem__gt=0).distinct("title")
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator | IsAdminUser,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly | IsAdminUser,)
        return super().get_permissions()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = Pagination

    # Метод создания жанра с проверкой на повторение
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

    # Автоматическое присвоение библиотекаря при создании книги
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator | IsAdminUser,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly | IsAdminUser,)
        return super().get_permissions()


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = Pagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator | IsAdminUser,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly | IsAdminUser,)
        return super().get_permissions()


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    pagination_class = Pagination

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator | IsAdminUser,)
        elif self.action == "list":
            self.permission_classes = (IsUserOwner | IsUserModerator,)
        return super().get_permissions()

    def perform_update(self, serializer):
        if self.request.data.get("keeper"):
            serializer.save(status="get")
        else:
            serializer.save(status="is_exist")

    def list(self, request, *args, **kwargs):
        queryset = BookItem.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GetBookView(APIView):
    def post(self, *args, **kwargs):
        queryset = BookItem.objects.get(number=self.request.data.get('number'))
        if queryset.keeper:
            print(queryset.number)
            print(self.request.data.get("number"))
            if queryset.keeper == self.request.user:
                return Response("Книга уже у вас", status=status.HTTP_200_OK)
            return Response("Нельзя выдать")
        queryset.status = "get"
        queryset.keeper = self.request.user
        queryset.save()
        return Response("Выдано", status=status.HTTP_200_OK)