from datetime import date

from sqlalchemy import select

from database.models.transaction import Transaction
from enums.transaction_type import TransactionType
from repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):

    def __init__(self, session):
        super().__init__(session, Transaction)

    def get_by_type(
        self,
        transaction_type: TransactionType,
    ):

        statement = (
            select(Transaction)
            .where(
                Transaction.transaction_type == transaction_type
            )
        )

        return self.session.scalars(statement).all()

    def get_by_category(
        self,
        category_id: int,
    ):

        statement = (
            select(Transaction)
            .where(
                Transaction.category_id == category_id
            )
        )

        return self.session.scalars(statement).all()

    def get_by_date_range(
        self,
        start_date: date,
        end_date: date,
    ):

        statement = (
            select(Transaction)
            .where(
                Transaction.transaction_date.between(
                    start_date,
                    end_date,
                )
            )
        )

        return self.session.scalars(statement).all()