# Тестовое задание с использованием Stripe [Тех. задание](https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit#)

## Описание
в данном проекте реализованы показ всех товаров (но в данном случает модель Item), и оплата каждого item:

  ```GET http://localhost:8000/item/1``` - открывается item с id = 1, с возможностью оплаты
  
  ```GET http://localhost:8000/items``` - открываются все items
  
  ```GET http://localhost:8000/buy/1``` -  session id
  
   ```GET http://localhost:8000/orders``` -  Все заказы
   
Заказы связаны с моделью Item

Добавлены переменные из .env файла. 

В панеле администратора добавлена визуальная тема admin-lite3. 

Так же добавлены модели Order, реализованы методы подсчета стоимости заказа с подсчетом стоимости каждой позиции

Проект был создан в учебных целях. Был использован стек:
Python, Django, Git, Bootstrap, SQLite

## Установка 
Клонируем репозиторий на локальную машину:

```$ git clone https://github.com/netshy/hw05_final```

 Создаем виртуальное окружение:
 
 ```$ python -m venv venv```  и активируем его  ```$ venv/Scripts/activate```
 
 Устанавливаем зависимости:

```$ pip install -r requirements.txt```

Создание и применение миграций:

```$ python manage.py makemigrations``` и ```$ python manage.py migrate```

Запускаем django сервер:

```$ python manage.py runserver```
