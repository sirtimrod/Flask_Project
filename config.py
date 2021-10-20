import os

# from dotenv import load_dotenv
# load_dotenv('')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///base.db')
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
