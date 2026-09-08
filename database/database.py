from database.base import Base

from database.connection import engine

from database.models.category import Category

from database.models.transaction import Transaction

from database.models.setting import Setting


def initialize_database():

    Base.metadata.create_all(
        bind=engine
    )

    """
    Cria todas as tabelas da aplicação caso ainda não existam.
    """