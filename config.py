import os

from dotenv import load_dotenv
load_dotenv('.env')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///base.db')

if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
