from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# Creating a binding to a DB to work with a DB
db_path = "sqlite:///base.db"
engine = create_engine(db_path)

# Session object
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base class object for model class
Base = declarative_base()
