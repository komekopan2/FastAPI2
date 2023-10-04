from sqlalchemy import create_engine
from api.db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from api.models.recipe import Base

# DB_URL = "mysql+pymysql://root:@db:3306/demo?charset=utf8"
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/demo?charset=utf8"

engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
