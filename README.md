# lang-python

Python practice

## Installing Python 3 on Mac OS

### Install or update Homebrew

*  open Terminal
*  `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* `brew -v`
* `brew update`

### Install GCC 

* Xcode or Command Line Tools

### Install Python via brew

* `brew install python` (/usr/local/lib/python3.7/site-packages)
* `brew upgrade python`
* set python 3 to default
  - `nano ~/.bash_profile` 
  - add : `alias python='python3'`
  - add : `alias pip='pip3'`  
  - `source ~/.bash_profile`
* symbolic link
  - `unlink /usr/local/bin/python`
  - `ln -s /usr/local/bin/python3.7 /usr/local/bin/python`
* `python --version` (3.7.7)

## Package Management

### Pip
* pip install pycodestyle
* pip freeze > requirements.txt
* pip install -r requirements.txt

### Virtualenv

If you already have a Python 3.5+ interpreter the best is to use pipx to install virtualenv into an isolated environment.

* Install virtualenv: `pip install virtualenv`  // pipx install virtualenv
* `virtualenv --version`
* `virtualenv --help`

### Pipenv

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. 
It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages.

* `pip install pipenv`
* Add the user base’s binary directory to PATH on Mac OS.
  - `nano ~/.bash_profile`
  - add : `export PATH=$PATH:/usr/local/lib/python3.7/site-packages/pipenv`
  - `source ~/.bash_profilepi`
* `pipenv install` // Pipfile, ~/.local/share/virtualenvs/
* `pipenv install requirements.txt`
* To activate this project's virtualenv, run `pipenv shell`. (/Users/jianpinggan/.local/share/virtualenvs/lang-python-jxL5W9ZT)
* run a command inside the virtualenv with `pipenv run python src/module/requests_mod.py`

## python packages

### pycodestyle

* pipenv install pycodestyle
* pipenv run pycodestyle src
* pipenv run pycodestyle --first --show-source --show-pep8 optparse.py


## Code Style

### Python Code Style Guide
* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.

### Naming Conventions
* Constants are written in uppercase letters
* Modules are required to have short, all-lowercase names
* Classes follow the capitalized words convention
* Exceptions follow the capitalized words convention
* local_var_name, global_var_name, instance_var_name
* method_name, function_name, function_parameter_name
* module_name, package_name
* ClassName, GLOBAL_CONSTANT_NAME, ExceptionName

## Learning Python Website
- https://stackabuse.com/introduction-to-the-python-coding-style/
- https://www.pythonforbeginners.com/
- https://www.learnpython.org
- https://github.com/michaelliao/learn-python3
- https://docs.python-guide.org
- http://news.51cto.com/art/201902/592006.htm
- https://docs.djangoproject.com/en/2.2/intro/tutorial01/
- https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
- https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5
