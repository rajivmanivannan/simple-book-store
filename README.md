# A simple book store app implementation using Python Flask + PostgreSQL

![Book Store](/screenshot/book-store.png)

## Virtual enverinment setup

```
$ brew install virtualenv

$ virtualenv --python=python3.7 env

$ source env/bin/activate
```

## To install required python libraries

```
$ pip install Flask flask_sqlalchemy flask_script flask_migrate psycopg2-binary Flask-WTF python-dotenv

or

$ pip install -r requirements.txt
```

## To Install PostgreSQL database and setup alias command in macOS

```
$ brew install postgresql

$ ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
```

### To setup alias command   

``` 
$ alias pg_start="launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist"  

$ alias pg_stop="launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist"
```

Here after you can use 'pg_start' command to start and use 'pg_stop' command to stop database service.  


## To setup database 

```
$ sudo -u whoami  psql postgres 

$ \password postgres 

> CREATE DATABASE books_store;
```

## To setup environment variable

Create .env file and add the below values  

```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://postgres:postgres@localhost/books_store"
```

## To setup database migration 
```

$ python manage.py db init

$ python manage.py db migrate

$ python manage.py db upgrade
```

## To run the applicaion 
```
$ FLASK_APP=app.py flask run
```    

## To freeze the python libraries 

```
$ pip freeze > requirements.txt
```

