# Онлайн-магазин комплектующих для ПК

Этот проект представляет собой онлайн-магазин, разработанный на Django, который предоставляет пользователям 
возможность просматривать, выбирать и заказывать комплектующие для ПК.

---

## 📋 Функционал

- **Главная страница**: просмотр категорий товаров.
- **Каталог товаров**: отображение товаров в выбранной категории с пагинацией.
- **Корзина**: добавление и удаление товаров, подсчет общей суммы.
- **Регистрация и аутентификация**: создание учетной записи и вход в систему.
- **Оформление заказа**: заполнение информации для доставки и подтверждение заказа.
- **Админ-панель**: управление категориями, товарами, заказами и пользователями.

---

## 🛠️ Технологии

Проект разработан с использованием следующих технологий:

- **Python** (версия 3.6+)
- **Django** (версия 4.2.17)
- **SQLite** — база данных для хранения данных о товарах, заказах и пользователях.
- **HTML**, **CSS** — для разработки интерфейса.
- **Django ORM** — для взаимодействия с базой данных.
- **Pillow** — для работы с изображениями.

---

## 🚀 Установка и настройка

### Требования
- Python 3.6+
- Установленный менеджер пакетов `pip`

### Установка

1. **Склонируйте репозиторий**:
   ```bash
   git clone https://git@github.com:Yarik72/projectDjangoSitePC.git
   ```
2. Создайте виртуальное окружение:
   ```bash
   python -m venv myvenv
   ```
3. Активируйте виртуальное окружение:
   - Windows:
     ```bash
     myvenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source myvenv/bin/activate
     ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Перейдите в директорию проекта:
   ```bash
   cd online-store
   ```
6. Примените миграции для базы данных:
   ```bash
   python manage.py migrate
   ```
7. Запустите локальный сервер:
   ```bash
   python manage.py runserver
   ```
   Откройте браузер и перейдите по адресу http://127.0.0.1:8000.

---

## 📂 Файловая структура

```
   online-store
   | db.sqlite3
   | manage.py
   |
   +---media
   |    +---categories
   |    |
   |    \---products
   +---online_store
   |    | asgi.py
   |    | settings.py
   |    | urls.py
   |    | wsgi.py
   |    | __init__.py
   |
   \---shop
    |   admin.py
    |   apps.py
    |   models.py
    |   tests.py
    |   views.py
    |   __init__.py
    |   
    +---migrations
    |   |   0001_initial.py
    |   |   __init__.py
    |   
    |           
    +---static
    |   \---css
    |           styles.css
    |           
    +---templates
           base.html
           cart.html
           category_list.html
           checkout.html
           login_page.html
           product_list.html
           registration_page.html
           
    
```

---

## 📄 Примеры страниц

- **Главная страница**: Отображает список категорий товаров с их изображениями.
- **Каталог товаров**:
  - Фильтрация товаров по категории.
  - Пагинация для удобного просмотра большого количества товаров.
- **Корзина**:
  - Просмотр добавленных товаров, их количества и общей стоимости.
  - Возможность удалить товар из корзины.
- **Регистрация и вход**:
  - Создание новой учетной записи.
  - Вход в систему с помощью имени пользователя и пароля.
- **Админ-панель**:
  - Управление категориями, товарами и заказами.

---

## 📦 Зависимости

```plaintext
asgiref==3.8.1
Django==4.2.17
django-debug-toolbar==4.4.6
pillow==11.0.0
pytz==2024.2
sqlparse==0.5.2
tzdata==2024.2

```

---

## 👤 Автор

Проект создан в рамках учебного проекта.  
Разработчик: [Ярослав Лазутин]

---

## 🔧 Дальнейшее развитие

- Добавление функционала оплаты онлайн.
- Реализация системы отзывов и рейтингов.
- Поиск и фильтрация товаров по различным параметрам.
- Отслеживание статуса доставки.

Спасибо за использование этого проекта! 🎉