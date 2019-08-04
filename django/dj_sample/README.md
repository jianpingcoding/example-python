# Get Start with dj_sample

## Requirement
- python 3
- pipenv

## Init environment
- pipenv install
- update database config in dj_sample/settings.py
- python manage.py migrate

## Run server
- python manage.py runserver 8080
- pipenv run python manage.py runserver 0:8000

## Available URLs :
- http://localhost:8080/polls/
- http://localhost:8080/polls/hello/joh
- http://localhost:8080/users/
- http://localhost:8080/users/?format=json
- http://localhost:8080/groups/

# Admin Module
## Create super user
* python manage.py createsuperuser
* admin:admin123
## Access admin
* http://127.0.0.1:8000/admin/.


# Create

## Creating projects
- django-admin startproject dj_sample

## Creating apps
- python manage.py startapp polls
- add 'polls.apps.PollsConfig' to INSTALLED_APPS in dj_sample/settings.py

## Create a simple service without model
- polls/views.py
```
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world!")
```
- polls/urls.py
```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
```
- dj_sample/urls.py
```
from django.urls import include, path
urlpatterns = [
    path('polls/', include('polls.urls'))
]
```

## Creating models
- polls/models.py


# Others

## Activating models
- python manage.py makemigrations polls
- python manage.py sqlmigrate polls 0001
- python manage.py migrate

## Playing with the API
- python manage.py shell
- from polls.models import Choice, Question
- Question.objects.all()

## Make app modifiable in the admin (app_name/admin.py)
```
from django.contrib import admin
from .models import Question
admin.site.register(Question)
```

# django rest framework
## Serializers

