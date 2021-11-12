web: gunicorn --bind 0.0.0.0:$PORT run_server:app
release: alembic upgrade head
release: docker-compose up
release: celery -A celery_worker worker -l INFO