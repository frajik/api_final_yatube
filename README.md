# Проект "АPI для Yatube"

## Описание проекта:
**Yatube** - проект соц.сети для публикации личных дневников.
**API для Yatube** - реализация API для всех моделей приложения. Aвторизованные пользователи могут публиковать и комментировать записи, подписываться и отписываться на/от других авторов. Реализована возможность поиска и фильтрации данных.

## Используемые технологии:
- [Python 3.7](https://www.python.org/)
- [DRF](https://www.django-rest-framework.org/)
- [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Djoser](https://djoser.readthedocs.io/en/latest/)

## Как запустить проект:
1. Клонируем репозиторий к себе на компьютер:
```
    git@github.com:frajik/api_final_yatube.git
```

2. Переходим в репозиторий:
```
    cd api_final_yatube
```

3. Создаем и активируем рабочее окружение:
```
    - python -m venv venv
    - source venv/scripts/activate
```

4. Устанавливаем зависимости из файла requirements.txt:
```
    - python -m pip install --upgrade pip
    -pip install -r requirements.txt
```

5. Выполняем миграции:
```
    - python manage.py migrate
```

6. Запускаем проект:
```
    - python manage.py runserver
```

## Примеры запросов:
- Пример POST-запроса с токеном Антона Чехова: добавление нового поста:
**POST .../api/v1/posts/**

- Пример ответа:
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
} 
```

- Пример GET-запроса: получаем информацию о группе:
**GET .../api/v1/groups/2/**

- Пример ответа:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
```

## Документация API:
- При запущенном проекте, для API Yatube, будет доступна полная документация, в формате Redoc, по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Автор:
**Матвейчук Дмитрий**