from sqlalchemy import func, select

from database.models.transaction import Transaction
from enums.transaction_type import TransactionType
from repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):

    def __init__(self, session):
        super().__init__(
            session,
            Transaction,
        )

    def get_by_type(
        self,
        transaction_type,
    ):

        return (
            self.session.query(self.model)
            .filter(
                self.model.transaction_type
                == transaction_type
            )
            .order_by(
                self.model.transaction_date.desc()
            )
            .all()
        )

    def get_by_type_and_date_range(
        self,
        transaction_type,
        start_date,
        end_date,
    ):

        return (
            self.session.query(self.model)
            .filter(
                self.model.transaction_type
                == transaction_type,

                self.model.transaction_date
                >= start_date,

                self.model.transaction_date
                <= end_date,
            )
            .order_by(
                self.model.transaction_date.desc()
            )
            .all()
        )

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

        return self.session.scalars(
            statement
        ).all()

    def get_by_date_range(
        self,
        start_date,
        end_date,
    ):

        return (
            self.session.query(self.model)
            .filter(
                self.model.transaction_date
                >= start_date,

                self.model.transaction_date
                <= end_date,
            )
            .order_by(
                self.model.transaction_date.desc()
            )
            .all()
        )

    def get_all_ordered(self):

        statement = (
            select(Transaction)
            .order_by(
                Transaction.transaction_date.desc()
            )
        )

        return self.session.scalars(
            statement
        ).all()

    def search_by_description(
        self,
        text,
    ):

        return (
            self.session.query(self.model)
            .filter(
                self.model.description.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                self.model.transaction_date.desc()
            )
            .all()
        )

    def get_filtered(
        self,
        transaction_type=None,
        start_date=None,
        end_date=None,
        search_text=None,
    ):

        query = self.session.query(
            self.model
        )

        if transaction_type is not None:

            query = query.filter(
                self.model.transaction_type
                == transaction_type
            )

        if start_date is not None:

            query = query.filter(
                self.model.transaction_date
                >= start_date
            )

        if end_date is not None:

            query = query.filter(
                self.model.transaction_date
                <= end_date
            )

        if search_text:

            query = query.filter(
                self.model.description.ilike(
                    f"%{search_text}%"
                )
            )

        return (
            query
            .order_by(
                self.model.transaction_date.desc()
            )
            .all()
        )

    def get_expense_total_by_category(
        self,
        category_id: int,
        start_date=None,
        end_date=None,
    ):

        statement = (
            select(
                func.coalesce(
                    func.sum(
                        Transaction.amount
                    ),
                    0,
                )
            )
            .where(
                Transaction.category_id
                == category_id,

                Transaction.transaction_type
                == TransactionType.EXPENSE,
            )
        )

        if start_date is not None:

            statement = statement.where(
                Transaction.transaction_date
                >= start_date
            )

        if end_date is not None:

            statement = statement.where(
                Transaction.transaction_date
                <= end_date
            )

        return self.session.scalar(
            statement
        )