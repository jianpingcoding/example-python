# example-python
Python example

# Python Style Guide
* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
## Naming Conventions
* Constants are written in uppercase letters
* Modules are required to have short, all-lowercase names
* Classes follow the capitalized words convention
* Exceptions follow the capitalized words convention
* Constants are written in uppercase letters


# Pip
## Installation
* pip install pycodestyle

## Usage
* pycodestyle --first --show-source --show-pep8 optparse.py
## Location
* /Users/jianpinggan/.virtualenvs/example-python/lib/python3.7/site-packages

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

# MariaDB
## Install on Mac
* brew install mariadb
## Start MariaDB server
* mysql.server start
* brew services start mariadb
* mysql -u root

# Related Website
* https://stackabuse.com/introduction-to-the-python-coding-style/
* https://www.pythonforbeginners.com/
* https://www.learnpython.org
* https://github.com/michaelliao/learn-python3