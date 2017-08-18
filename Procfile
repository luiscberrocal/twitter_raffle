web: gunicorn config.wsgi:application
worker: celery worker --app=twitter_raffle.taskapp --loglevel=info
