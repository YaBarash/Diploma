from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Author(models.Model):
    """
    Модель Автора с поляем полного имени
    """
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
    """
    Модель Жанра с полем названия
    """
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
    """
    Модель Книги с полями названия, описания, жанра, автора и библиотекарем
    """
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
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="библиотекарь",
        help_text="укажите библиотекаря",
    )

    # Метод подсчета экземпляров книг, чтобы обращаться к нему как к свойству при помощи декоратора
    @property
    def count_item(self):
        return self.bookitem_set.count()

    def __str__(self):
        return (
                ",".join(self.authors.values_list("full_name", flat=True))
                + f": {self.title}"
        )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"


class BookItem(models.Model):
    """
    Модель Экземпляра Книги с полями инвентарного номера, книги, держателя и статуса книги
    """
    number = models.PositiveIntegerField(
        primary_key=True,
        verbose_name="Инвентарный номер",
        help_text="Введите инвентарный номер",
    )
    book_details = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Название книги",
        help_text="Введите название книги",
    )
    keeper = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
        verbose_name="держатель",
        help_text="Выберите держателя",
        **NULLABLE,
    )

    status = models.CharField(
        max_length=20,
        choices=[('is_exist', 'в наличии'), ('get', 'выдана'), ('lost', 'утеряна')],
        verbose_name='Статус книги',
        help_text='Статус книги',
        default='is_exist')

    def __str__(self):
        return f"Инвентарный номер: {self.number}, Инфо книги: {self.book_details}, держатель {self.keeper} {self.status}"

    class Meta:
        verbose_name = "Экземпляр книги"
        verbose_name_plural = "Экземпляры книги"
