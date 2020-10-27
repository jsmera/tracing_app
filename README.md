NUTRIPEDIA
==========

Behold My Awesome Project!

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Settings
--------

### Pre-instalation
- [Postgres (Version 11.XX or higher)](https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-18-04-es#paso-1-instalar-postgresql)
- Python (Version 3.6 or higher)
- wkhtmltopdf

### Create DB
First, create a role and a database, the database has to be owned by the role I create or the role must have permissions on it. Remember to save the role's password.

```sql
create role username_name with createdb login encrypted password 'password';
create database database_name owner username_name;
```

### Install requirements
On the project's path run:
```shell
  $ pip install -r requirements/local.txt
```

### Configure database
On the project's path create a file named `.env` with the following content

```dot
DATABASE_URL=postgres://username_name:password@127.0.0.1:5432/database_name
```
### Migrate
On the project's path run:
```shell
  $ python manage.py migrate
```

### Running server
On the project's path run:
```shell
  $ python manage.py runserver
```

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)

Basic Commands
--------------

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out
    the form. Once you submit it, you'll see a "Verify Your E-mail
    Address" page. Go to your console to see a simulated email
    verification message. Copy the link into your browser. Now the
    user's email should be verified and ready to go.

-   To create an **superuser account**, use this command::

```shell
  $ python manage.py createsuperuser
```

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.


Deploy
--------
1. Install Heroku
2. Login to Heroku
3. In the root path, execute ```heroku create```
4. ```git push heroku master```
5. ```heroku open```

ENVIROMENT
--------

```
DJANGO_SETTINGS_MODULE=config.settings.production
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_PASSWORD=nutripedia1999
EMAIL_HOST_USER=barberprocesos@gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
WKHTMLTOPDF_CMD=<wkhtmltopdf's path>
```
