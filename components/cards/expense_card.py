from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
)

from components.cards.base_card import BaseCard


class ExpenseCard(BaseCard):

    delete_requested = Signal(int)

    def __init__(
        self,
        transaction_id: int,
        title: str,
        amount: float,
        transaction_date: str,
        category_name: str,
    ):
        super().__init__()

        self.transaction_id = transaction_id
        self.title = title
        self.amount = amount
        self.transaction_date = transaction_date
        self.category_name = category_name

        self._setup_ui()

    def _setup_ui(self):

        self._create_header()
        self._create_amount()
        self._create_date()
        self._create_category()

    def _create_header(self):

        header_layout = QHBoxLayout()

        title = QLabel(self.title)
        title.setObjectName("expenseTitle")

        self.delete_button = QPushButton("🗑")
        self.delete_button.setObjectName(
            "deleteButton"
        )

        self.delete_button.clicked.connect(
            self._request_delete
        )

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(
            self.delete_button
        )

        self.layout.addLayout(
            header_layout
        )

    def _create_amount(self):

        amount = QLabel(
            f"R$ {self.amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        amount.setObjectName(
            "expenseAmount"
        )

        self.layout.addWidget(amount)

    def _create_date(self):

        date_label = QLabel(
            f"📅 {self.transaction_date}"
        )

        date_label.setObjectName(
            "expenseDate"
        )

        self.layout.addWidget(
            date_label
        )

    def _create_category(self):

        category = QLabel(
            self.category_name
        )

        category.setObjectName(
            "expenseCategory"
        )

        self.layout.addWidget(
            category
        )

    def _request_delete(self):

        self.delete_requested.emit(
            self.transaction_id
        )