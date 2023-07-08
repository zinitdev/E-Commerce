<div align="center">
  <a href="https://flask.palletsprojects.com/en/2.3.x/">
    <img src="https://flask.palletsprojects.com/en/2.3.x/_images/flask-horizontal.png" alt="Flask" width="300"> 
    </a>
</div>

# E-commerce® Website

## Hello, Bro ✌️

The reason I chose Flask for this project :

-   Work on smaller projects (single-page)
-   Have varied database support, including NoSQL
-   Have flexibility and freedom to choose libraries and extensions
-   Have API support or want to add new extensions in the future
-   Create static websites, rapid prototypes, and RESTful web services

## Key Features

**Public User**

-   Search Product
-   View Product
-   Create User Account
-   Sigin User
-   Add Product to Cart

**Signin User**

-   Search Product
-   View Product
-   Create Order
-   Can View View, UPDATE and DELETE Orders
-   Payment
-   Post Comment

**Admin**

-   Signin
-   Search
-   CRUD Product
-   Statistical & Report
-   See all Orders
-   Manage all User

## Getting started

Use the virtual environment `.venv` :

-   virtualenv

```bash
pip install virtualenv
```

-   .venv

```bash
python -m venv .venv
.venv\Scripts\activate
```

requirements.txt

-   Export requirements:

```bash
pip freeze > requirements.txt
```

-   Install requirements:

```bash
pip install -r requirements.txt
```

Run project

-   Set `FLASK_APP` environment variable is used to specify how to load the application.

```bash
set FLASK_APP=app.py
```

## Flask Plugins

-   [Flask](https://pypi.org/project/Flask/) - Flask framework 🌶