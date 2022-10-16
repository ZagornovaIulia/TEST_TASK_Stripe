# Test task using Stripe 
### Description
  In the implementation of the project, displays of all goods are implemented (but the Item model is implemented in the implementation), and payment for each product:
  Cover orders with Item model
  Added variables from .env file.
  The admin-lite3 visual theme has been added to the admin panel.
  Also added order models, applied cost calculation methods with calculation of the cost of each position
  
---

### Technologies:
* Python
* Django
* Pytest
* Git
* DRF
* JWT

---

### Installation
Clone the repository on the local machine:

```$ git clone https://github.com/vkletkin/yatube-main```

 Create a virtual environment:
 
 ```$ python -m venv venv```
 
 Install dependencies:

```$ pip install -r requirements.txt```

Creating and applying migrations:

```$ python manage.py makemigrations``` and  ```$ python manage.py migrate```

Starting the django server:

```$ python manage.py runserver```

---


## URL examples

```GET http://localhost:8000/item/1 - opens item with id = 1, with payment option
  
  GET http://localhost:8000/items - open all items
  
  GET http://localhost:8000/buy/1 - session id
  
  GET http://localhost:8000/orders - All orders```
