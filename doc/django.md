# Django
## Install
* pip install Django
* python -m django --version
## Create a project
* django-admin startproject djangoproject
## Create the app
* python manage.py startapp polls
## The development server
* python manage.py runserver 8080
* python manage.py runserver 0:8000
## Database setup
* pip3 install mysqlclient
* python manage.py migrate
## Model
* python manage.py makemigrations polls
* python manage.py sqlmigrate polls 0001
## Admin
* python manage.py createsuperuser
* admin:admin123
* http://127.0.0.1:8000/admin/.
