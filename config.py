import os

from dotenv import load_dotenv
load_dotenv('.env')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///base.db')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
