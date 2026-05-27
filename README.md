# Интернет-магазин на FastAPI

## Описание проекта

Проект представляет собой веб-приложение интернет-магазина с backend-частью на FastAPI и frontend-частью на HTML/CSS/JavaScript. Приложение позволяет управлять товарами: просматривать, добавлять, редактировать и удалять товары. Данные хранятся в PostgreSQL, ORM - SQLAlchemy.

Проект разработан в рамках учебного курса и демонстрирует навыки работы с FastAPI, PostgreSQL, SQLAlchemy, Git и GitHub.

## Основные возможности

- **CRUD операции с товарами:**
  - Получение списка всех товаров (GET /products)
  - Получение товара по ID (GET /products/{id})
  - Добавление нового товара (POST /products)
  - Обновление данных товара (PUT /products/{id})
  - Удаление товара (DELETE /products/{id})

- **Веб-интерфейс:**
  - Страница для просмотра всех товаров
  - Форма для добавления новых товаров
  - Возможность редактирования и удаления товаров
  - Визуальное выделение товаров с остатком менее 5 штук

- **Валидация данных:**
  - Цена товара должна быть больше 0
  - Количество товара не может быть отрицательным
  - Название товара обязательно для заполнения

- **Тестирование:**
  - Тесты для всех эндпоинтов
  - Используется отдельная тестовая база данных

## Стек технологий

| Технология | Назначение |
|------------|------------|
| Python 3.14 | Язык программирования |
| FastAPI | Веб-фреймворк |
| PostgreSQL | База данных |
| SQLAlchemy | ORM |
| Alembic | Миграции |
| Pydantic | Валидация данных |
| Pytest | Тестирование |
| Uvicorn | ASGI-сервер |
| HTML/CSS/JS | Фронтенд |

## Структура проекта

Store_2/
├── app/
│ ├── init.py
│ ├── main.py # Основной файл приложения
│ ├── crud.py # CRUD операции с БД
│ ├── database.py # Настройка подключения к БД
│ ├── models.py # SQLAlchemy модели
│ └── schemas.py # Pydantic схемы
├── static/
│ └── index.html # Фронтенд интерфейс
├── tests/
│ └── test_main.py # Тесты
├── alembic/ # Миграции
├── .env # Переменные окружения
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md


## Переменные окружения

Создайте файл `.env` в корне проекта:

DB_USER=postgres
DB_PASSWORD=ваш_пароль
DB_HOST=localhost
DB_PORT=5432
DB_NAME=shop_db


## Как запустить проект

### 1. Клонировать репозиторий

git clone https://github.com/Vladiktpu/Store_2.git
cd Store_2

2. Создать виртуальное окружение

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Установить зависимости

pip install -r requirements.txt

4. Настроить базу данных PostgreSQL

CREATE DATABASE shop_db;

5. Настроить файл .env

Заполните файл .env своими данными для подключения к БД

6. Применить миграции

alembic upgrade head

7. Запустить сервер

uvicorn app.main:app --reload

http://localhost:8000

## Авторы

- [![GitHub](https://img.shields.io/badge/Влад-181717?style=flat&logo=github)](https://github.com/Vladiktpu)
- [![GitHub](https://img.shields.io/badge/Женя-181717?style=flat&logo=github)](https://github.com/zheny77)
- [![GitHub](https://img.shields.io/badge/Женя-181717?style=flat&logo=github)](https://github.com/zheny77)

