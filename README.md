# Diploma

Дипломный проект DF1 "API для управления библиотекой"

### Описание задачи:

Разработка REST API для управления библиотекой. API предоставляет возможности для управления книгами,
авторами и пользователями, а также для отслеживания выдачи книг пользователям.
Для реализации API применяется Django Rest Framework (DRF).

### Функционал API:

1. **Управление книгами**:
    - Создание, редактирование и удаление книг.
    - Получение списка всех книг.
    - Поиск книг по различным критериям (название, автор, жанр и т.д.).
2. **Управление авторами**:
    - Создание, редактирование и удаление авторов.
    - Получение списка всех авторов.
3. **Управление пользователями**:
    - Регистрация и авторизация пользователей.
    - Получение информации о пользователях.
4. **Выдача книг**:
    - Запись информации о выдаче книги пользователю.
    - Отслеживание статуса возврата книги

### Технические требования:

1. Запустить докер комнадой

* `docker run -p 8080:80 nginx:latest`

2. Задать настройки приложения в

* `docker-compose.yaml`

3. Заполнение файла .env согласно примеру (.env.template)
4. Создать образ и запустить контейнеры

* `docker-compose up -d --build`

5. Проверяем работоспособность в браузере

* `http://localhost:8000/swagger/`

### Работа с приложением:

1. Для начала работы необходимо зарегестрироваться на платформе по эндпоинту

* `/users/register/`
   ```json
	{
		"email": "your_email",
		"password": "your_password",
	}
	```

2. Войти в учетную запись для получения JWT-токена по эндпоинту

* `/users/login/`
	```json
	{
		"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMzMwODUwMywiaWF0IjoxNzMzMjIyMTAzLCJqdGkiOiIzODI1YTExN2E5NDg0MWNhOTg4MDg0OGY5ODVjMWRjOCIsInVzZXJfaWQiOjF9.Ac6H0LjNQRbq3EUHwRdcJooLvQPz3zpUcC2xQ2Ge9pc",
		"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzMzA4NTAzLCJpYXQiOjE3MzMyMjIxMDMsImp0aSI6IjJhMTRhNDZiOTgzMTRmNDA4ZmQ2MDM3Y2M3N2Q0ZWMwIiwidXNlcl9pZCI6MX0.UC4phtaMVzjnI_pWg6rM9cOYqIo9RIbU0ciidjPU6sk"
	}
	```

3. Данный токен вставляется для работы в эндпоинтах с моделями Book, Authors и BookItem с помощью заголовка Authorization со
   значением Bearer <access token>



