from rest_framework import serializers
from book.models import Book, Author, Genre, BookItem


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            "title",
            "authors",
        )


class GenreSerializer(serializers.ModelSerializer):
    genre = BookSerializer

    class Meta:
        model = Genre
        fields = "__all__"


class BookItemSerializer(serializers.ModelSerializer):
    book_details = BookSerializer

    class Meta:
        model = BookItem
        fields = "__all__"
