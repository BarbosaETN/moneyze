from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
)

from components.cards.base_card import BaseCard

from enums.transaction_type import (
    TransactionType,
)


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

        self.setObjectName(
            "historyCard"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout.setContentsMargins(
            28,
            18,
            28,
            18,
        )

        self.layout.setSpacing(
            20
        )

        self._create_content()

    def _create_content(self):

        row_layout = QHBoxLayout()

        row_layout.setSpacing(
            20
        )

        self._create_date(
            row_layout
        )

        self._create_title(
            row_layout
        )

        self._create_category(
            row_layout
        )

        self._create_amount(
            row_layout
        )

        self.layout.addLayout(
            row_layout
        )

    def _create_date(
        self,
        layout,
    ):

        date_label = QLabel(
            self.transaction_date
        )

        date_label.setObjectName(
            "historyDate"
        )

        date_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            date_label,
            2,
        )

    def _create_title(
        self,
        layout,
    ):

        title_label = QLabel(
            self.title
        )

        title_label.setObjectName(
            "historyTitle"
        )

        title_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            title_label,
            4,
        )

    def _create_category(
        self,
        layout,
    ):

        category_label = QLabel(
            self.category_name
        )

        category_label.setObjectName(
            "historyCategory"
        )

        category_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            category_label,
            2,
        )

    def _create_amount(
        self,
        layout,
    ):

        amount_label = QLabel(
            self._format_currency()
        )

        amount_label.setObjectName(
            self._get_amount_object_name()
        )

        amount_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            amount_label,
            2,
        )

    def _format_currency(self):

        prefix = (
            "+"
            if self.transaction_type
            == TransactionType.INCOME
            else "-"
        )

        formatted_amount = (
            f"{self.amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return (
            f"{prefix}R$ "
            f"{formatted_amount}"
        )

    def _get_amount_object_name(
        self,
    ):

        if (
            self.transaction_type
            == TransactionType.INCOME
        ):

            return (
                "historyIncomeAmount"
            )

        return (
            "historyExpenseAmount"
        )