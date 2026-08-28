import qtawesome as qta

from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
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

        self.setObjectName(
            "expenseCard"
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

        self._create_description(
            row_layout
        )

        self._create_category(
            row_layout
        )

        self._create_amount(
            row_layout
        )

        self._create_delete_button(
            row_layout
        )

        self.layout.addLayout(
            row_layout
        )

    def _create_description(
        self,
        layout,
    ):

        description_layout = QHBoxLayout()

        description_layout.setSpacing(
            14
        )

        self._create_icon()

        text_layout = QVBoxLayout()

        text_layout.setSpacing(
            4
        )

        title_label = QLabel(
            self.title
        )

        title_label.setObjectName(
            "expenseTitle"
        )

        date_label = QLabel(
            self.transaction_date
        )

        date_label.setObjectName(
            "expenseDate"
        )

        text_layout.addWidget(
            title_label
        )

        text_layout.addWidget(
            date_label
        )

        description_layout.addWidget(
            self.icon_container
        )

        description_layout.addLayout(
            text_layout
        )

        description_layout.addStretch()

        layout.addLayout(
            description_layout,
            4,
        )

    def _create_icon(self):

        self.icon_container = QLabel()

        self.icon_container.setObjectName(
            "expenseIcon"
        )

        self.icon_container.setFixedSize(
            34,
            34,
        )

        self.icon_container.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        icon = qta.icon(
            "fa5s.arrow-down",
            color="#F87171",
        )

        self.icon_container.setPixmap(
            icon.pixmap(
                16,
                16,
            )
        )

    def _create_category(
        self,
        layout,
    ):

        category_label = QLabel(
            self.category_name
        )

        category_label.setObjectName(
            "expenseCategory"
        )

        category_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
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
            "expenseAmount"
        )

        amount_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            amount_label,
            2,
        )

    def _create_delete_button(
        self,
        layout,
    ):

        self.delete_button = QPushButton()

        self.delete_button.setObjectName(
            "expenseDeleteButton"
        )

        self.delete_button.setFixedSize(
            36,
            36,
        )

        icon = qta.icon(
            "fa5s.trash",
            color="#94A3B8",
        )

        self.delete_button.setIcon(
            icon
        )

        self.delete_button.clicked.connect(
            self._request_delete
        )

        layout.addWidget(
            self.delete_button
        )

    def _format_currency(self):

        formatted_amount = (
            f"{self.amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return f"- R$ {formatted_amount}"

    def _request_delete(self):

        self.delete_requested.emit(
            self.transaction_id
        )