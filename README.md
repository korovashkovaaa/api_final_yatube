# YaTube API

REST API для социальной сети YaTube. Пользователи могут публиковать посты, подписываться на других пользователей, комментировать записи и просматривать ленту избранных авторов.

## 🚀 Возможности

- Регистрация и JWT-аутентификация пользователей
- CRUD-операции с постами
- Комментарии к постам
- Система подписок
- Просмотр ленты подписок

## 🔧 Установка и запуск

```bash
git clone https://github.com/yourusername/api_final_yatube.git
cd api_final_yatube
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver