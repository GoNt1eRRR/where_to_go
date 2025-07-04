# Куда пойти?

Данный проект это интерактивная карта Москвы, на которой отмечены интересные места для посещения и отдыха с подробным описанием локации

![Image](https://github.com/user-attachments/assets/83316d43-eb92-4e01-b907-2ef98a244708)

## Особенности проекта
- Удобная админ-панель для добавления локаций, включая загрузку фотографий.
- Возможность редактирования уже добавленных записей.
- Поддержка расширенного форматирования описания благодаря встроенному редактору.
- Быстрая загрузка новых мест через JSON-файлы.

Пример редактора:
![Image](https://github.com/user-attachments/assets/a77792d3-fdd2-4f04-8fa0-fe100d360fd0)

Пример JSON с данными:
```python
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```

Для загрузки данных в базу воспользуйтесь:
```python
python manage.py load_place <ссылка_на_json>
```

Чтобы получить прямую ссылку на JSON-файл на GitHub, нажмите кнопку Raw при просмотре файла.

## Требования
- Python 3.7+
- Django 4+
- Установленные зависимости из requirements.txt

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/GoNt1eRRR/where_to_go
```
2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Создайте файл для переменных окружения в корне проекта .env. Переменные окружения:
```bash
SECRET_KEY=<ваш_секретный_ключ>
```
Ниже представлены переменные окружения, которые имеют значения по умолчанию. При необходимости можно устанавливать на свои.
```python
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
```
Ниже приведены ссылки на официальную документацию Django по переменным окружения:

- [SECRET_KEY](https://docs.djangoproject.com/en/5.2/ref/settings/#secret-key)
- [DEBUG](https://docs.djangoproject.com/en/5.2/ref/settings/#debug)
- [ALLOWED_HOSTS](https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts)
- [STATIC_URL](https://docs.djangoproject.com/en/5.2/ref/settings/#static-url)
- [STATIC_ROOT](https://docs.djangoproject.com/en/5.2/ref/settings/#static-root)
- [MEDIA_URL](https://docs.djangoproject.com/en/5.2/ref/settings/#media-url)
- [MEDIA_ROOT](https://docs.djangoproject.com/en/5.2/ref/settings/#media-root)

5. Примените миграции:
```python
python manage.py migrate
```
6. Создайте суперпользователя:
```python
python manage.py createsuperuser
```
7. Запустите сервер:
```python
python manage.py runserver
```

## Демо-версия сайта
Данные в картах взяты из [репозитория](https://github.com/devmanorg/where-to-go-places)

Демо-версия [Сайта](https://gont1er.pythonanywhere.com/)

