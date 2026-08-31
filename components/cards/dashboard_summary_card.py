import qtawesome as qta

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from components.cards.base_card import (
    BaseCard,
)


class DashboardSummaryCard(BaseCard):

    def __init__(
        self,
        title: str,
        amount: float,
        icon_name: str,
        icon_color: str,
        icon_background: str,
        variation_text: str,
        variation_color: str,
    ):
        super().__init__()

        self.title = title
        self.amount = amount

        self.icon_name = icon_name
        self.icon_color = icon_color
        self.icon_background = icon_background

        self.variation_text = variation_text
        self.variation_color = variation_color

        self.setObjectName(
            "dashboardSummaryCard"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout.setContentsMargins(
            18,
            18,
            18,
            18,
        )

        self.layout.setSpacing(
            0
        )

        self._create_header()
        self._create_amount()
        self._create_variation()

    def _create_header(self):

        header_layout = QHBoxLayout()

        header_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        title_label = QLabel(
            self.title
        )

        title_label.setObjectName(
            "dashboardSummaryTitle"
        )

        header_layout.addWidget(
            title_label
        )

        header_layout.addStretch()

        icon_container = QWidget()

        icon_container.setObjectName(
            "dashboardSummaryIcon"
        )

        icon_container.setFixedSize(
            36,
            36,
        )

        icon_container.setStyleSheet(
            f"""
            QWidget#dashboardSummaryIcon {{
                background-color: {self.icon_background};
                border-radius: 10px;
            }}
            """
        )

        icon_layout = QVBoxLayout(
            icon_container
        )

        icon_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        icon_label = QLabel()

        icon_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        icon = qta.icon(
            self.icon_name,
            color=self.icon_color,
        )

        icon_label.setPixmap(
            icon.pixmap(
                18,
                18,
            )
        )

        icon_layout.addWidget(
            icon_label
        )

        header_layout.addWidget(
            icon_container
        )

        self.layout.addLayout(
            header_layout
        )

    def _create_amount(self):

        self.amount_label = QLabel(
            self._format_currency(
                self.amount
            )
        )

        self.amount_label.setObjectName(
            "dashboardSummaryAmount"
        )

        self.amount_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
        )

        self.layout.addSpacing(
            12
        )

        self.layout.addWidget(
            self.amount_label
        )

    def _create_variation(self):

        self.variation_label = QLabel(
            self.variation_text
        )

        self.variation_label.setObjectName(
            "dashboardSummaryVariation"
        )

        self.variation_label.setStyleSheet(
            f"""
            color: {self.variation_color};
            """
        )

        self.layout.addSpacing(
            10
        )

        self.layout.addWidget(
            self.variation_label
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

    def update_variation(
        self,
        variation_text: str,
    ):

        self.variation_text = variation_text

        self.variation_label.setText(
            variation_text
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

        return (
            f"R$ {formatted_amount}"
        )