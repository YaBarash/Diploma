# Generated by Django 5.1.3 on 2024-11-26 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0003_alter_book_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Укажите название жанра",
                        max_length=50,
                        verbose_name="Название жанра",
                    ),
                ),
            ],
            options={
                "verbose_name": "жанр",
                "verbose_name_plural": "жанры",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                default=2,
                help_text="укажите жанр книги",
                on_delete=django.db.models.deletion.CASCADE,
                to="book.genre",
                verbose_name="жанр",
            ),
            preserve_default=False,
        ),
    ]
