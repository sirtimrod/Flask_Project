import os


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///base.db')

if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
EXTERNAL_IP_URL = 'https://api64.ipify.org/'
COUNTRY_CODE_URL = 'http://api.ipstack.com/'
ACCESS_KEY = '74a3ef2e0e526908b52d42f40bd961ef'
