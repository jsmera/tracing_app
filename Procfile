release: python manage.py migrate
web: gunicorn config.wsgi:application --log-file -
worker: celery worker -A config -l --loglevel=INFO