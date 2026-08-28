from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QWidget,
)


class ExpenseHeader(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "expenseHeader"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            20,
            0,
            20,
            0,
        )

        layout.setSpacing(
            0
        )

        description_label = QLabel(
            "DESCRIÇÃO"
        )

        description_label.setObjectName(
            "transactionHeaderLabel"
        )

        category_label = QLabel(
            "CATEGORIA"
        )

        category_label.setObjectName(
            "transactionHeaderLabel"
        )

        amount_label = QLabel(
            "VALOR"
        )

        amount_label.setObjectName(
            "transactionHeaderLabel"
        )

        layout.addWidget(
            description_label,
            4,
        )

        layout.addWidget(
            category_label,
            2,
        )

        layout.addWidget(
            amount_label,
            2,
        )