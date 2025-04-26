from sqlalchemy import create_engine, insert
from src.domain.client.user import User, Address
from src.infrastructure.base import Base
from sqlalchemy.orm import sessionmaker
from decouple import config

USERNAME = config("POSTGRES_USERNAME")
PASSWORD = config("POSTGRES_PASSWORD")
HOST = config("POSTGRES_HOST")
PORT = config("POSTGRES_PORT")
DATABASE = config("POSTGRES_DATABASE")

url = f"{HOST}:{PORT}"


def connect():
    try:
        engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{url}/{DATABASE}")
        Base.metadata.create_all(engine)
    except ConnectionError as err:
        print(err)


if __name__ == "__main__":
    connect()
