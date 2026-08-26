from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
)

from components.cards.base_card import BaseCard
from enums.transaction_type import TransactionType


class HistoryCard(BaseCard):

    def __init__(
        self,
        title: str,
        amount: float,
        category_name: str,
        transaction_date: str,
        transaction_type: TransactionType,
    ):
        super().__init__()

        self.title = title
        self.amount = amount
        self.category_name = category_name
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout()

        self._create_date(layout)
        self._create_title(layout)
        self._create_category(layout)
        self._create_amount(layout)

        self.layout.addLayout(layout)

    def _create_date(self, layout):

        date_label = QLabel(
            self.transaction_date
        )

        date_label.setObjectName(
            "historyDate"
        )

        layout.addWidget(date_label)

    def _create_title(self, layout):

        title = QLabel(self.title)

        title.setObjectName(
            "historyTitle"
        )

        layout.addWidget(title)

    def _create_category(self, layout):

        category = QLabel(
            self.category_name
        )

        category.setObjectName(
            "historyCategory"
        )

        layout.addWidget(category)

    def _create_amount(self, layout):

        is_income = (
            self.transaction_type
            == TransactionType.INCOME
        )

        prefix = "+" if is_income else "-"

        amount_text = (
            f"{prefix} R$ "
            f"{self.amount:,.2f}"
        )

        amount_text = (
            amount_text
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        amount = QLabel(amount_text)

        amount.setObjectName(
            "historyIncomeAmount"
            if is_income
            else "historyExpenseAmount"
        )

        layout.addWidget(amount)