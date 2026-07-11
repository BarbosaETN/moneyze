from database.base import Base
from database.connection import engine

from database.models.category import Category
from database.models.transaction import Transaction

def initialize_database():
    Base.metadata.create_all(bind=engine)