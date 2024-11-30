from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from book.models import Book, Author, Genre
from book.paginators import Pagination
from book.permissions import IsUserModerator
from book.serializers import BookSerializer, AuthorSerializer, GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "authors__full_name", "genre__title"]

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        return super().get_permissions()

    """Условие поиска по названию, автору, жанру в разных регистрах
    Сделать проверку на повтор 
    
    Условие по показу книг в наличии (count!=0)
    Если книги нет в наличии писать сообщение (скоро появятся)
    Отслеживание статуса книги (когда выдана, кому, когда отдать)
    Уменьшать счетчик по количеству свободных книг
    Исправить на постргскл, требование диплома
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
                'error': f'Ошибка с кодом 400. Объект с названием {lower_title} уже существует'
            }
            return JsonResponse(data["error"], safe=False, status=status.HTTP_400_BAD_REQUEST, json_dumps_params={'ensure_ascii': False})

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

    def get_permissions(self):
        if self.action in ["update", "retrieve", "create", "destroy"]:
            self.permission_classes = (IsUserModerator,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        return super().get_permissions()
