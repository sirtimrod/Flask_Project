web: gunicorn --bind 0.0.0.0:$PORT run_server:app
release: alembic upgrade head
worker: celery -A celery_worker worker --loglevel=info