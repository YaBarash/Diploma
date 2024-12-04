# Generated by Django 5.1.3 on 2024-12-03 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0009_book_count"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="count",
        ),
        migrations.AddField(
            model_name="bookitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("is_exist", "в наличии"),
                    ("get", "выдана"),
                    ("lost", "утеряна"),
                ],
                default="is_exist",
                help_text="Статус книги",
                max_length=20,
                verbose_name="Статус книги",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="owner",
            field=models.ForeignKey(
                help_text="укажите библиотекаря",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="библиотекарь",
            ),
        ),
        migrations.AlterField(
            model_name="bookitem",
            name="keeper",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Выберите держателя",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="держатель",
            ),
        ),
    ]
