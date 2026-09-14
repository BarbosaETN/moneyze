from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_PATH

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_session():
    return SessionFactory()