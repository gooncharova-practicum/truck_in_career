# Тестовое задание "Самосвалы в карьере"

## Описание
Веб-приложение, позволяющее узнать сколько руды в данный момент перевозят самосвалы и имеет ли место перегруз. 
Список можно фильтровать по моделям. Самосвалы, их модели и рейсы можно добавлять через админку.

## Используемые технологии
- Django 4.1.4

## Запуск приложения
Есть 2 варианта. Первый с помощью docker:

1. Установите <a href="https://docs.docker.com">docker.</a>
2. Склонируйте репозиторий c помощью SSH или HTTPS
3. Зайдите в директорию с проектом.
4. Выполните команду: `cp ./env.example ./env` <br>
Заполните создавшийся .env файл
5. Запуск осуществляется командой: <br>
`docker-compose up --build -d` или `make up`

Второй - с помощью виртуального окружения:

1. Склонируйте репозиторий c помощью SSH или HTTPS
2. Зайдите в директорию с проектом.
3. Выполните команду: `cp ./env.example ./env` <br>
Заполните создавшийся .env файл
4. Выполните команду `python -m venv venv`
5. Активируйте виртуальное окружение: `source venv/bin/activate`
6. Установите зависимости `pip install -r requirements.txt`
7. Создайте суперюзера `python manahe.py createsuperuser`
8. Запустите сервер `python manahe.py runserver`

Приложение будет доступно по адресу `127.0.0.1:8000`

## Тестовый логин/пароль для админки
Логин - admin
Пароль - Admin12345