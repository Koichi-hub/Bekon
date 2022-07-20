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
DEBUG=False
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
- `pipenv shell`
- `docker-compose -f docker-compose.prod.yml up -d --build`
- `docker ps` - копируем container_id bekon_app
- `docker exec -it <container_id> /bin/sh`
- `python manage.py migrate`
- `python manage.py collectstatic`
- `exit`
- переходим на http://localhost/
- `docker-compose -f docker-compose.prod.yml down -v` чтобы остановить
- `docker images` - список образов 
- `docker rmi bekon_app bekon_nginx`  - удаление образов

## Об этом
Проект незакончен. У меня не хватило денег чтобы продолжить разработку и дойти до части с чатом и REST API. У меня сейчас не простое время и когда деньги появятся возможно я закончу проект или просто продолжу другие на NodeJS
