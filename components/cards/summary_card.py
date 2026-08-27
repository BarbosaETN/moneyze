import qtawesome as qta

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from components.buttons.primary_button import PrimaryButton
from components.cards.base_card import BaseCard


class SummaryCard(BaseCard):

    action_requested = Signal()

    def __init__(
        self,
        title: str,
        amount: float,
        icon_name: str,
        icon_color: str,
        icon_background: str,
        button_text: str | None = None,
        button_icon: str | None = None,
    ):
        super().__init__()

        self.title = title
        self.amount = amount
        self.icon_name = icon_name
        self.icon_color = icon_color
        self.icon_background = icon_background
        self.button_text = button_text
        self.button_icon = button_icon

        self.setObjectName(
            "summaryCard"
        )

        self._setup_ui()

    def _setup_ui(self):

        main_layout = QHBoxLayout()

        main_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        main_layout.setSpacing(
            16
        )

        self._create_icon()

        content_layout = QVBoxLayout()

        content_layout.setSpacing(
            4
        )

        title_label = QLabel(
            self.title
        )

        title_label.setObjectName(
            "summaryTitle"
        )

        self.amount_label = QLabel(
            self._format_currency(
                self.amount
            )
        )

        self.amount_label.setObjectName(
            "summaryAmount"
        )

        content_layout.addWidget(
            title_label
        )

        content_layout.addWidget(
            self.amount_label
        )

        main_layout.addWidget(
            self.icon_container
        )

        main_layout.addLayout(
            content_layout
        )

        main_layout.addStretch()

        if self.button_text:

            self.action_button = PrimaryButton(
                self.button_text,
                self.button_icon,
            )

            self.action_button.clicked.connect(
                self.action_requested.emit
            )

            main_layout.addWidget(
                self.action_button
            )

        self.layout.addLayout(
            main_layout
        )

    def _create_icon(self):

        self.icon_container = QLabel()

        self.icon_container.setObjectName(
            "summaryIcon"
        )

        self.icon_container.setFixedSize(
            54,
            54,
        )

        self.icon_container.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.icon_container.setStyleSheet(
            f"""
            QLabel#summaryIcon {{
                background-color: {self.icon_background};
                border-radius: 14px;
            }}
            """
        )

        icon = qta.icon(
            self.icon_name,
            color=self.icon_color,
        )

        pixmap = icon.pixmap(
            24,
            24,
        )

        self.icon_container.setPixmap(
            pixmap
        )

    def update_amount(
        self,
        amount: float,
    ):

        self.amount = amount

        self.amount_label.setText(
            self._format_currency(
                amount
            )
        )

    def _format_currency(
        self,
        amount: float,
    ):

        formatted_amount = (
            f"{amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return f"R$ {formatted_amount}"