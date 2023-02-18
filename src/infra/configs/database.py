""" database url """
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

USER = os.getenv("DB_USER")
PWD =  os.getenv("DB_PWD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB =   os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def make_database():
    """create models"""
    Base.metadata.create_all(bind=engine)


def get_database():
    """get database connection"""
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
