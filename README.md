<a id="anchor"></a>
# Room Reservation

## Описание:
Приложение предоставляет возможность бронировать помещения на определённый период времени.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone
```

```
cd room_reservation
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Создать файл .env в корне проекта:

```
APP_TITLE=Ваше название проекта
APP_DESCRIPTION=Ваше описание проекта
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET='my_secret'
FIRST_SUPERUSER_EMAIL='admin@admin.com'
FIRST_SUPERUSER_PASSWORD='superuser'
```


[__В начало__](#anchor) :point_up:
