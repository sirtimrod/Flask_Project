release: alembic upgrade head
web: gunicorn --bind 0.0.0.0:$PORT run_server:app
release: celery -A celery_worker worker --loglevel=info --concurrency=1