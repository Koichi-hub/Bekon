# Bekon
Социальная сеть для программистов

## Стек
- Django, gunicorn
- Nginx
- PostgreSQL
- Docker, docker-compose

## Запуск
- клонируем репо и переходим в папку проекта
- создаем файл `.env` с содержанием:
```
DEBUG=1
SECRET_KEY=<ваш секрет кей>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
CSRF_TRUSTED_ORIGINS=http://localhost:80 http://localhost:8000

SQL_ENGINE=django.db.backends.postgresql_psycopg2
SQL_DATABASE=bekon 
SQL_USER=bekon
SQL_PASSWORD=password

SQL_HOST=db
SQL_PORT=5432
```
- `docker-compose -f docker-compose.dev.yml up -d --build`
- переходим на http://localhost:8000/

## Мой авторский дизайн
[Figma](https://www.figma.com/file/yXeQBq60ZjMhAuqwagJVo9/Bekon)
