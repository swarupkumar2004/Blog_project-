📝 Django Blog API

A simple RESTful API backend for a blogging platform, built using Django and Django REST Framework. This project includes features like user authentication, user roles (admin/user), blog post creation, and post management (CRUD).


🚀 Features

User Registration & Login (Token-based using JWT)

Role-based access (Admin / Normal User)

Create, Read, Update, Delete blog posts

API tested using Thunder Client / Postman

MySQL as the database

Permissions & Authentication using DRF



📂 Project Structure

blog_project/
├── blog/                  # Main blog app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── blog_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── requirements.txt


⚙ Setup Instructions

✅ Step 1: Clone the repository

git clone https://github.com/your-username/blog-api.git
cd blog-api

✅ Step 2: Create & activate virtual environment

python -m venv venv
venv\Scripts\activate    # Windows

✅ Step 3: Install dependencies

pip install -r requirements.txt

✅ Step 4: Configure database (MySQL in settings.py)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

✅ Step 5: Run migrations

python manage.py makemigrations
python manage.py migrate

✅ Step 6: Create superuser

python manage.py createsuperuser

✅ Step 7: Run the server

python manage.py runserver


🔐 Authentication (JWT)

Signup: /api/signup/

Login (Token): /api/token/

Refresh Token: /api/token/refresh/


Include token in headers as:

Authorization: Bearer <your_token>


📮 API Endpoints

Method	Endpoint	Description

GET	/api/posts/	List all blog posts
POST	/api/posts/	Create a new post
PUT	/api/posts/<id>/	Update a post
DELETE	/api/posts/<id>/	Delete a post



👤 Roles & Permissions

Admin: Can view/edit/delete all posts

User: Can view and manage only their own posts



🧪 API Testing Tools

Thunder Client (VSCode)

Postman


🛠 Built With

Python 3.11+

Django 4.2+

Django REST Framework

PostgreSQL

JWT Authentication
