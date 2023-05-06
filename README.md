# Практический проект Django REST API

Данный проект представляет собой API для трёх приложений books, posts и todo. Проект выполнен по книге "Django for APIs" William S. Vincent с целью дополнительной практики в Django REST API. 

# Функциональность API

Для приложения books была добавлена возможность получения списка всех книг, создание новой книги, редактирование и удаление существующих книг.

Для приложения posts была добавлена возможность получения списка всех постов, создание нового поста, редактирование и удаление существующих постов. Также была добавлена возможность получения детальной информации о посте по его ID.

Для приложения todo была добавлена возможность получения списка всех задач, создание новой задачи, редактирование и удаление существующих задач. Также была добавлена возможность получения детальной информации о задаче по ее ID.

Для всех приложений были добавлены тесты для проверки функциональности API.

# Установка и запуск проекта

1. Склонируйте репозиторий на свой компьютер:


git clone https://github.com/black-water715/api_project_test.git


2. Создайте виртуальное окружение и активируйте его:


python -m venv env
source env/bin/activate (для Linux/Mac) или env\Scripts\activate.bat (для Windows)


3. Установите зависимости:


pip install -r requirements.txt


4. Создайте базу данных:


python manage.py migrate


5. Запустите сервер:


python manage.py runserver


6. Для доступа к API необходимо получить токен авторизации. Для этого создайте суперпользователя:


python manage.py createsuperuser


7. Перейдите по адресу http://127.0.0.1:8000/admin/ и войдите в админ-панель, используя учетные данные суперпользователя.

8. Создайте нового пользователя и выдайте ему права на просмотр и изменение данных для нужных приложений.

9. Получите токен авторизации для нового пользователя, перейдя по адресу http://127.0.0.1:8000/api/token/ и введя логин и пароль нового пользователя.

10. Для доступа к API используйте полученный токен авторизации.

# Используемые технологии

* Python 3
* Django 3
* Django Rest Framework 3
* SQLite

# Автор

* **black-water715** - [GitHub](https://github.com/black-water715)
