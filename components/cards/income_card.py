import qtawesome as qta

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from components.cards.base_card import BaseCard


class IncomeCard(BaseCard):

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
            "incomeCard"
        )

        self._setup_ui()

    def _setup_ui(self):

        self._create_content()

    def _create_content(self):

        content_layout = QHBoxLayout()

        content_layout.setContentsMargins(
            20,
            16,
            20,
            16,
        )

        content_layout.setSpacing(
            16
        )

        self._create_icon()

        description_layout = QVBoxLayout()

        description_layout.setSpacing(
            4
        )

        title = QLabel(
            self.title
        )

        title.setObjectName(
            "incomeTitle"
        )

        date_label = QLabel(
            self.transaction_date
        )

        date_label.setObjectName(
            "incomeDate"
        )

        description_layout.addWidget(
            title
        )

        description_layout.addWidget(
            date_label
        )

        category = QLabel(
            self.category_name
        )

        category.setObjectName(
            "incomeCategory"
        )

        amount = QLabel(
            self._format_currency()
        )

        amount.setObjectName(
            "incomeAmount"
        )

        amount.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )

        self._create_delete_button()

        content_layout.addWidget(
            self.icon_container
        )

        content_layout.addLayout(
            description_layout,
            4,
        )

        content_layout.addWidget(
            category,
            2,
        )

        content_layout.addWidget(
            amount,
            2,
        )

        content_layout.addWidget(
            self.delete_button
        )

        self.layout.addLayout(
            content_layout
        )

    def _create_icon(self):

        self.icon_container = QLabel()

        self.icon_container.setObjectName(
            "incomeIcon"
        )

        self.icon_container.setFixedSize(
            32,
            32,
        )

        self.icon_container.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        icon = qta.icon(
            "fa5s.arrow-up",
            color="#34D399",
        )

        pixmap = icon.pixmap(
            16,
            16,
        )

        self.icon_container.setPixmap(
            pixmap
        )

    def _create_delete_button(self):

        self.delete_button = QPushButton()

        self.delete_button.setObjectName(
            "incomeDeleteButton"
        )

        self.delete_button.setFixedSize(
            32,
            32,
        )

        self.delete_button.setIcon(
            qta.icon(
                "fa5s.trash",
                color="#94A3B8",
            )
        )

        self.delete_button.clicked.connect(
            self._request_delete
        )

    def _format_currency(self):

        formatted_amount = (
            f"{self.amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return f"+R$ {formatted_amount}"

    def _request_delete(self):

        self.delete_requested.emit(
            self.transaction_id
        )