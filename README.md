# Environment Setup
## Install Homebrew on Mac OS
- open Terminal
- /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- brew -v
## Install Python 3 on Mac OS
- Before installing Python, it need to install GCC : Xcode or Command Line Tools
- brew install python
- nano ~/.bash_profile : export PATH="/usr/local/opt/python/libexec/bin:$PATH"
- python --version
## Install Pipenv on Mac OS
- pip install --user pipenv
- add the user base’s binary directory to PATH.
  - python -m site --user-base  : the path is ~/Library/Python/3.7
  - nano ~/.bash_profile : export PATH=$PATH:~/Library/Python/3.7/bin
## Install virtualenv on Mac OS
- pip install virtualenv
- virtualenv --version
## Install on Mac
- brew install mariadb


# Useful Command
## Python 3 on Mac OS
- brew upgrade python
- python --version
## Pipenv on Mac OS
- cd project_folder
- pipenv install requests
- pipenv run python src/module/requests_mod.py
## Virtualenv on Mac OS
- cd project_folder
- virtualenv venvyo
- virtualenv -p /usr/bin/python2.7 venv
- source venv/bin/activate
- deactivate
## MariaDB
- mysql.server start
- brew services start mariadb
- mysql -u root
## Pip
- pip install pycodestyle
- pip install requests
## Pycodestyle
- pycodestyle --first --show-source --show-pep8 optparse.py


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


# Learning Python Website
- https://stackabuse.com/introduction-to-the-python-coding-style/
- https://www.pythonforbeginners.com/
- https://www.learnpython.org
- https://github.com/michaelliao/learn-python3
- https://docs.python-guide.org
