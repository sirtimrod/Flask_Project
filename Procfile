web: gunicorn --bind 0.0.0.0:$PORT run_server:app
release: alembic upgrade head
worker: celery worker --app=celery_worker.app