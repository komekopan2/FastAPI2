from sqlalchemy import create_engine
from api.db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, Base
from sqlalchemy.exc import OperationalError, InternalError
from sqlalchemy.sql import text

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?charset=utf8"
DEMO_DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/demo?charset=utf8"

engine = create_engine(DEMO_DB_URL, echo=True)


def database_exists():
    try:
        engine.connect()
        return True
    except (OperationalError, InternalError) as e:
        print(e)
        print("Database does not exist")
        return False


def create_database():
    if not database_exists():
        root = create_engine(DB_URL, echo=True)
        with root.connect() as conn:
            conn.execute(text("CREATE DATABASE demo;"))
        print("Database created")
    Base.metadata.create_all(bind=engine)
    print("Tables created")


if __name__ == "__main__":
    create_database()
