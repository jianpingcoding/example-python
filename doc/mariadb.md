# Install MariaDB

## Installing MariaDB on Mac OS
- Install or update Homebrew
  - open Terminal
  - /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  - brew -v
  - brew update
- Install with homebrew
  - brew install mariadb
- Setting Path
  - nano ~/.bash_profile
  - export PATH=$PATH:/usr/local/Cellar/mariadb/10.4.6/support-files
  - source ~/.bash_profile

# MariaDB command
- ./mysql.server start
- ./mysql -u root
- ./mysql.server stop
- brew services start mariadb
- mysql.server start
- mysql -u root