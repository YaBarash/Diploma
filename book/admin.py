from django.contrib import admin
from book.models import Book, Author, Genre, BookItem


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "title",
        "authors",
        "genre",
    )


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


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "book_details",
        "keeper",
        "qr_code"
    )
