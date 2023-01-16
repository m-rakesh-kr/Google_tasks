import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

""" DATABASE SETTINGS
  >>>> https://docs.sqlalchemy.org/en/
   1) set the current server config.
   2) create the sqlalchemy engine.
   3) create the sessionmaker object.
   4) define the declarative base.
"""
# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog_data.db"

engine = create_engine(os.environ.get('DB_URL'), echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

Base = declarative_base()


def get_db():
    """
    This method is used to create the database instance.
    :return: database instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
