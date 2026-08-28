from datetime import date

from enums.transaction_type import TransactionType

from exceptions.not_found_error import (
    NotFoundError,
)

from exceptions.validation_error import (
    ValidationError,
)

from services.base_service import BaseService


class TransactionService(BaseService):

    def __init__(self, repository):
        super().__init__(
            repository
        )

    def create(self, **data):

        self._validate(data)

        return super().create(
            **data
        )

    def get_incomes(
        self,
        start_date=None,
        end_date=None,
    ):

        if (
            start_date is not None
            and end_date is not None
        ):

            return (
                self.repository
                .get_by_type_and_date_range(
                    TransactionType.INCOME,
                    start_date,
                    end_date,
                )
            )

        return self.repository.get_by_type(
            TransactionType.INCOME
        )

    def get_expenses(
        self,
        start_date=None,
        end_date=None,
    ):

        if (
            start_date is not None
            and end_date is not None
        ):

            return (
                self.repository
                .get_by_type_and_date_range(
                    TransactionType.EXPENSE,
                    start_date,
                    end_date,
                )
            )

        return self.repository.get_by_type(
            TransactionType.EXPENSE
        )

    def get_expenses_by_date_range(
        self,
        start_date,
        end_date,
    ):

        return (
            self.repository
            .get_by_type_and_date_range(
                TransactionType.EXPENSE,
                start_date,
                end_date,
            )
        )

    def delete_by_id(
        self,
        transaction_id,
    ):

        transaction = self.get_by_id(
            transaction_id
        )

        if transaction is None:

            raise NotFoundError(
                "Transação não encontrada."
            )

        return super().delete(
            transaction
        )

    def _validate(self, data):

        title = data.get(
            "title"
        )

        if not title or not title.strip():

            raise ValidationError(
                "O título da transação é obrigatório."
            )

        amount = data.get(
            "amount"
        )

        if amount is None:

            raise ValidationError(
                "O valor da transação é obrigatório."
            )

        if amount <= 0:

            raise ValidationError(
                (
                    "O valor da transação deve "
                    "ser maior que zero."
                )
            )

        transaction_type = data.get(
            "transaction_type"
        )

        if not isinstance(
            transaction_type,
            TransactionType,
        ):

            raise ValidationError(
                "O tipo da transação é inválido."
            )

        transaction_date = data.get(
            "transaction_date"
        )

        if not isinstance(
            transaction_date,
            date,
        ):

            raise ValidationError(
                "A data da transação é obrigatória."
            )

        category_id = data.get(
            "category_id"
        )

        if (
            transaction_type == TransactionType.EXPENSE
            and category_id is None
        ):

            raise ValidationError(
                (
                    "A categoria da despesa "
                    "é obrigatória."
                )
            )