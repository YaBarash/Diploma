from rest_framework import serializers
from book.models import Book, Author, Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "authors",
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
