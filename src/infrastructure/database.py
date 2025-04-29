from sqlalchemy import create_engine
from src.infrastructure.persistence.common.base import Base
from sqlalchemy.orm import Session
from decouple import config
import functools
from src.infrastructure.persistence.schemes import *

USERNAME = config("POSTGRES_USERNAME")
PASSWORD = config("POSTGRES_PASSWORD")
HOST = config("POSTGRES_HOST")
PORT = config("POSTGRES_PORT")
DATABASE = config("POSTGRES_DATABASE")

url = f"{HOST}:{PORT}"


def connect(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            engine = create_engine(
                f"postgresql://{USERNAME}:{PASSWORD}@{url}/{DATABASE}"
            )
            with Session(engine) as session:
                _func = func(session=session, *args, **kwargs)
                session.commit()
                return _func
        except ConnectionError as err:
            print(err)

    return wrapper


def make_tabels():
    try:
        engine = create_engine(
            f"postgresql://{USERNAME}:{PASSWORD}@{url}/{DATABASE}", echo=True
        )
        Base.metadata.create_all(engine)

    except ConnectionError as err:
        print(err)


if __name__ == "__main__":
    make_tabels()
