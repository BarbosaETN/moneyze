from collections import defaultdict
from datetime import date

from enums.transaction_type import (
    TransactionType,
)


class ReportService:

    def __init__(
        self,
        transaction_repository,
    ):

        self.transaction_repository = (
            transaction_repository
        )

    def get_income_expense_by_month(
        self,
        year: int,
    ):

        start_date = date(
            year,
            1,
            1,
        )

        end_date = date(
            year,
            12,
            31,
        )

        transactions = (
            self.transaction_repository
            .get_by_date_range(
                start_date,
                end_date,
            )
        )

        monthly_data = defaultdict(
            lambda: {
                "income": 0,
                "expense": 0,
            }
        )

        for transaction in transactions:

            month = (
                transaction
                .transaction_date
                .month
            )

            if (
                transaction.transaction_type
                == TransactionType.INCOME
            ):

                monthly_data[
                    month
                ]["income"] += (
                    transaction.amount
                )

            elif (
                transaction.transaction_type
                == TransactionType.EXPENSE
            ):

                monthly_data[
                    month
                ]["expense"] += (
                    transaction.amount
                )

        return (
            self._format_monthly_data(
                monthly_data
            )
        )

    def _format_monthly_data(
        self,
        monthly_data,
    ):

        month_labels = [
            "Jan",
            "Fev",
            "Mar",
            "Abr",
            "Mai",
            "Jun",
            "Jul",
            "Ago",
            "Set",
            "Out",
            "Nov",
            "Dez",
        ]

        result = []

        for month in range(
            1,
            13,
        ):

            result.append(
                {
                    "month": month,
                    "label": (
                        month_labels[
                            month - 1
                        ]
                    ),
                    "income": (
                        monthly_data[
                            month
                        ]["income"]
                    ),
                    "expense": (
                        monthly_data[
                            month
                        ]["expense"]
                    ),
                }
            )

        return result

    def get_expense_distribution_by_category(
        self,
        year: int,
    ):

        start_date = date(
            year,
            1,
            1,
        )

        end_date = date(
            year,
            12,
            31,
        )

        transactions = (
            self.transaction_repository
            .get_by_type_and_date_range(
                TransactionType.EXPENSE,
                start_date,
                end_date,
            )
        )

        category_data = defaultdict(
            lambda: 0
        )

        for transaction in transactions:

            category_name = (
                transaction.category.name
                if transaction.category
                else "Sem categoria"
            )

            category_data[
                category_name
            ] += transaction.amount

        return [
            {
                "category": category,
                "amount": amount,
            }
            for category, amount
            in category_data.items()
        ]