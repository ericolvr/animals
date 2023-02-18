import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.infra.configs.database import get_database
from src.main import app

load_dotenv()


USER = os.getenv("TEST_DB_USER")
PWD = os.getenv("TEST_DB_PWD")
HOST = os.getenv("TEST_DB_HOST")
PORT = os.getenv("TEST_DB_PORT")
NAME = os.getenv("TEST_DB_NAME")

print(USER, PWD, HOST, PORT, NAME)


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:secret@localhost:3307/tests"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_database():
    """get database connection"""
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_database] = override_get_database
