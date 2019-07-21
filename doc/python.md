# Install Python

## Installing Python 3 on Mac OS
- Install or update Homebrew
  - open Terminal
  - /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  - brew -v
  - brew update
- Install GCC : 
  - Xcode or Command Line Tools
- brew install python (/usr/local/lib/python3.7/site-packages)
- brew upgrade python
- Setup PATH
  - nano ~/.bash_profile 
  - add : alias python='python3'
  - add : alias pip='pip3'
  - source ~/.bash_profile
- symbolic link
  - unlink /usr/local/bin/python
  - ln -s /usr/local/bin/python3.7 /usr/local/bin/python
- python --version

## Installing Pipenv on Mac OS
- pip install pipenv ()
- add the user base’s binary directory to PATH.
  - nano ~/.bash_profile 
  - add : export PATH=$PATH:/usr/local/lib/python3.7/site-packages/pipenv
  - source ~/.bash_profilepi
  
## Installing virtualenv on Mac OS
- pip install virtualenv
- virtualenv --version


# Package Management and Virtual Environment support

## Pip
- pip install pycodestyle
- pip freeze > requirements.txt
- pip install -r requirements.txt

## Pipenv 
- cd project_folder
- pipenv install // ~/.local/share/virtualenvs/
- pipenv install --dev
- pipenv run python src/module/requests_mod.py
- pipenv shell
- pipenv install requirements.txt

## Virtualenv on Mac OS
- cd project_folder
- virtualenv venvyo
- virtualenv -p /usr/bin/python2.7 venv
- source venv/bin/activate
- deactivate


# python package usage
## Pycodestyle
- pycodestyle --first --show-source --show-pep8 optparse.py
