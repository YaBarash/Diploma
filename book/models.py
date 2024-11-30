from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Author(models.Model):
    full_name = models.CharField(
        max_length=50,
        verbose_name="полное имя автора",
        help_text="введите имя автора",
        unique=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"


class Genre(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название жанра",
        help_text="Укажите название жанра",
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="название",
        help_text="Укажите название",
    )
    description = models.TextField(
        max_length=300,
        **NULLABLE,
        verbose_name="описание",
        help_text="введите описание",
    )
    genre = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="жанр",
        help_text="укажите жанр книги",
    )
    authors = models.ManyToManyField(
        Author, verbose_name="автор", help_text="укажите автора"
    )
    count = models.PositiveIntegerField(
        verbose_name="количество книг в наличии",
        help_text="укажите количество книг в наличии",
        default=0,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="владелец",
        help_text="укажите собственника",
    )

    def __str__(self):
        return (
            ",".join(self.authors.values_list("full_name", flat=True))
            + f": {self.title}"
        )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
