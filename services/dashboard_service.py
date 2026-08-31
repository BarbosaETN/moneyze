from datetime import (
    date,
    timedelta,
)

from enums.transaction_type import (
    TransactionType,
)


class DashboardService:

    def __init__(
        self,
        transaction_repository,
        category_repository,
    ):

        self.transaction_repository = (
            transaction_repository
        )

        self.category_repository = (
            category_repository
        )

    def get_summary(
        self,
    ):

        comparison_totals = (
            self._get_comparison_totals()
        )

        accumulated_balance = (
            self._get_total_balance()
        )

        return {
            "total_balance": (
                comparison_totals[
                    "current_balance"
                ]
            ),

            "current_balance": (
                comparison_totals[
                    "current_balance"
                ]
            ),

            "previous_balance": (
                comparison_totals[
                    "previous_balance"
                ]
            ),

            "total_income": (
                comparison_totals[
                    "current_income"
                ]
            ),

            "total_expense": (
                comparison_totals[
                    "current_expense"
                ]
            ),

            "accumulated_balance": (
                accumulated_balance
            ),

            "balance_variation": (
                comparison_totals[
                    "balance_variation"
                ]
            ),

            "income_variation": (
                comparison_totals[
                    "income_variation"
                ]
            ),

            "expense_variation": (
                comparison_totals[
                    "expense_variation"
                ]
            ),
        }

    def get_category_summary(
        self,
    ):

        today = date.today()

        start_date = (
            today.replace(
                day=1
            )
        )

        categories = (
            self.category_repository.get_all()
        )

        category_summary = []

        for category in categories:

            spent = (
                self.transaction_repository
                .get_expense_total_by_category(
                    category_id=category.id,
                    start_date=start_date,
                    end_date=today,
                )
            )

            percentage = (
                self._calculate_percentage(
                    spent,
                    category.budget,
                )
            )

            category_summary.append(
                {
                    "name": category.name,
                    "budget": category.budget,
                    "spent": spent,
                    "percentage": percentage,
                }
            )

        return category_summary

    def _calculate_total(
        self,
        transactions,
        transaction_type,
    ):

        return sum(
            transaction.amount
            for transaction in transactions
            if (
                transaction.transaction_type
                == transaction_type
            )
        )

    def _calculate_percentage(
        self,
        value: float,
        total: float,
    ):

        if total <= 0:

            return 0

        return (
            value / total
        ) * 100

    def get_cash_flow(
        self,
    ):

        transactions = (
            self.transaction_repository
            .get_all()
        )

        months = (
            self._get_last_months(
                6
            )
        )

        cash_flow = []

        for year, month in months:

            income = 0
            expense = 0

            for transaction in transactions:

                transaction_date = (
                    transaction.transaction_date
                )

                if (
                    transaction_date.year == year
                    and transaction_date.month == month
                ):

                    if (
                        transaction.transaction_type
                        == TransactionType.INCOME
                    ):

                        income += (
                            transaction.amount
                        )

                    elif (
                        transaction.transaction_type
                        == TransactionType.EXPENSE
                    ):

                        expense += (
                            transaction.amount
                        )

            balance = (
                income
                - expense
            )

            cash_flow.append(
                {
                    "label": (
                        self._get_month_label(
                            month
                        )
                    ),

                    "income": income,
                    "expense": expense,
                    "balance": balance,
                }
            )

        return cash_flow

    def _get_last_months(
        self,
        total_months: int,
    ):

        today = date.today()

        months = []

        year = today.year
        month = today.month

        for _ in range(
            total_months
        ):

            months.append(
                (
                    year,
                    month,
                )
            )

            month -= 1

            if month == 0:

                month = 12

                year -= 1

        months.reverse()

        return months

    def _get_month_label(
        self,
        month: int,
    ):

        month_labels = {
            1: "Jan",
            2: "Fev",
            3: "Mar",
            4: "Abr",
            5: "Mai",
            6: "Jun",
            7: "Jul",
            8: "Ago",
            9: "Set",
            10: "Out",
            11: "Nov",
            12: "Dez",
        }

        return (
            month_labels[month]
        )

    def _get_comparison_periods(
        self,
    ):

        today = date.today()

        current_start = (
            today.replace(
                day=1
            )
        )

        previous_month_end = (
            current_start
            - timedelta(
                days=1
            )
        )

        previous_start = (
            previous_month_end.replace(
                day=1
            )
        )

        comparison_day = min(
            today.day,
            previous_month_end.day,
        )

        previous_end = (
            previous_start.replace(
                day=comparison_day
            )
        )

        return {
            "current_start": current_start,
            "current_end": today,
            "previous_start": previous_start,
            "previous_end": previous_end,
        }

    def _get_period_total(
        self,
        transaction_type,
        start_date,
        end_date,
    ):

        transactions = (
            self.transaction_repository
            .get_by_type_and_date_range(
                transaction_type,
                start_date,
                end_date,
            )
        )

        return sum(
            transaction.amount
            for transaction in transactions
        )

    def _get_comparison_totals(
        self,
    ):

        periods = (
            self._get_comparison_periods()
        )

        current_income = (
            self._get_period_total(
                TransactionType.INCOME,
                periods["current_start"],
                periods["current_end"],
            )
        )

        previous_income = (
            self._get_period_total(
                TransactionType.INCOME,
                periods["previous_start"],
                periods["previous_end"],
            )
        )

        current_expense = (
            self._get_period_total(
                TransactionType.EXPENSE,
                periods["current_start"],
                periods["current_end"],
            )
        )

        previous_expense = (
            self._get_period_total(
                TransactionType.EXPENSE,
                periods["previous_start"],
                periods["previous_end"],
            )
        )

        income_variation = (
            self._calculate_variation(
                current_income,
                previous_income,
            )
        )

        expense_variation = (
            self._calculate_variation(
                current_expense,
                previous_expense,
            )
        )

        current_balance = (
            current_income
            - current_expense
        )

        previous_balance = (
            previous_income
            - previous_expense
        )

        balance_variation = (
            self._calculate_variation(
                current_balance,
                previous_balance,
            )
        )

        return {
            "current_income": current_income,
            "previous_income": previous_income,
            "income_variation": income_variation,

            "current_expense": current_expense,
            "previous_expense": previous_expense,
            "expense_variation": expense_variation,

            "current_balance": current_balance,
            "previous_balance": previous_balance,
            "balance_variation": balance_variation,
        }

    def _calculate_variation(
        self,
        current_value: float,
        previous_value: float,
    ):

        if previous_value == 0:

            return None

        variation = (
            (
                current_value
                - previous_value
            )
            / previous_value
        ) * 100

        return variation

    def _get_total_balance(
        self,
    ):

        transactions = (
            self.transaction_repository
            .get_all()
        )

        total_income = (
            self._calculate_total(
                transactions,
                TransactionType.INCOME,
            )
        )

        total_expense = (
            self._calculate_total(
                transactions,
                TransactionType.EXPENSE,
            )
        )

        return (
            total_income
            - total_expense
        )