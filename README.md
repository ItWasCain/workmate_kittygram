# Тестовое задание для Workmate

### Общее описание проекта:
Проект представляет web службу на основе REST архитектуры.
Данные передаются в формате JSON.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ItWasCain/workmate_kittygram.git
cd workmate_kittygram/infra/
```

Запустить проект в Docker, выполнить миграции и собрать статику:
```
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
```

Для тестирования API - загрузить тестовые данные.
В других случаях эту команду можно пропустить.
```
docker compose exec backend python manage.py import_test_data
```

Создать суперпользователя:
```
docker compose exec backend python manage.py createsuperuser
```

### API
Проект доступен по ссылке http://localhost:8000/api/
API доступен только после регистрации и получения ключа.
```
POST http://localhost:8000/api/auth/users/
{
    "username": "YourName",
    "password": "YourPassword"
}
```

```
POST http://localhost:8000/api/auth/jwt/create/
{
    "username": "YourName",
    "password": "YourPassword"
}
```

### Документация
Swagger - http://localhost:8000/swagger/
Redoc - http://localhost:8000/redoc/

### Использованные технологии:

    Python, Django, Django Rest Framework, PostgeSQL, Docker.


### Разработчик:
Никита Песчанов https://github.com/ItWasCain

