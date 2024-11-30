from django.contrib import admin
from book.models import Book, Author, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "title",
        "authors",
        "genre",
    )
    # search_fields = ('title', 'author__authors', 'genre__genre',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
