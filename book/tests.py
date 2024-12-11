from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class AuthorTestCase(APITestCase):
    def setUp(self):
        self.author = {"full_name": "А.С. Пушкин"}
        # self.genre = {"title": "Проза"}
        # self.book = {"title": "Дубровский", "author": self.author, "genre": self.genre}

        # Создаем пользователя
        self.user = User.objects.create(
            email="alina@mail.ru",
            password="123qwe",
            is_staff=True,
            is_active=True,
        )

        # Аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_author(self):
        response = self.client.post('/library/authors/', self.author)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
