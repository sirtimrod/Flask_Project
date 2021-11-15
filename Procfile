release: alembic upgrade head
release: celery -A celery_worker worker --detach
web: gunicorn --bind 0.0.0.0:$PORT run_server:app