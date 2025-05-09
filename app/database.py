from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Параметры подключения к БД
username = ""
password = ""  # Пароль из docker-compose.yml
host = ""  # Имя сервиса БД в docker-compose.yml
port = ""  # Внутренний порт PostgreSQL
database = ""
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Base = automap_base()
# Base.prepare(autoload_with=engine) #point associate the DB engine with the Auto-map base.

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
