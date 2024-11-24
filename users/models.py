from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = PhoneNumberField(
        region="RU", **NULLABLE, verbose_name="Телефон", help_text="Укажите телефон"
    )
    avatar = models.ImageField(
        upload_to="users/avatar/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


def __str__(self):
    return self.email


class Meta:
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"
