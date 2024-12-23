# Generated by Django 5.1.3 on 2024-11-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_alter_book_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="full_name",
            field=models.CharField(
                help_text="введите имя автора",
                max_length=50,
                unique=True,
                verbose_name="полное имя автора",
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="title",
            field=models.CharField(
                help_text="Укажите название жанра",
                max_length=50,
                unique=True,
                verbose_name="Название жанра",
            ),
        ),
    ]
