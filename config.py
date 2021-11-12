import os


DB_FOLDER = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(DB_FOLDER, 'base.db')}")

if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
IP_INF_URL = 'https://ipapi.co/'
# CELERY_BROKER_URL = 'amqp://user:user@localhost:5672'
CELERY_BROKER_URL = 'amqps://ovekxwlm:I4k5t49G1wDBEYxGD-al8yGl5HrLDShY@jaguar.rmq.cloudamqp.com/ovekxwlm'
RESULT_BACKEND = "db+" + SQLALCHEMY_DATABASE_URI
