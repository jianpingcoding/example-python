# Django

## Install
### pip install
- pip install Django
- python -m django --version
### pipenv install
- pipenv install Django
- pipenv run python -m django --version

## Create a project
- django-admin startproject project_name

## The development server
- python manage.py runserver 8080
- python manage.py runserver 0:8000

## Project settings (project_name/settins.py)
### Timezone setting
```
TIME_ZONE = 'Asia/Singapore'
```

## Database
### Install mysql client
- pip3 install mysqlclient
### Mysql project setting
```
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'djangodb',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '',
  }
}
```
### Database migrate 
- python manage.py makemigrations
- python manage.py migrate

## Admin app
### Create super user
- python manage.py createsuperuser
- admin:admin123
### Access admin
- http://127.0.0.1:8000/admin/.

## App
### Creating a new app
- python manage.py startapp app_name
### App migration
- python manage.py makemigrations app_name
- python manage.py sqlmigrate polls 0001


