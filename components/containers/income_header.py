from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QWidget,
)


class IncomeHeader(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "incomeHeader"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            68,
            14,
            68,
            14,
        )

        description = QLabel(
            "DESCRIÇÃO"
        )

        description.setObjectName(
            "incomeHeaderLabel"
        )

        category = QLabel(
            "CATEGORIA"
        )

        category.setObjectName(
            "incomeHeaderLabel"
        )

        amount = QLabel(
            "VALOR"
        )

        amount.setObjectName(
            "incomeHeaderLabel"
        )

        amount.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        layout.addWidget(
            description,
            4,
        )

        layout.addWidget(
            category,
            2,
        )

        layout.addWidget(
            amount,
            2,
        )

        layout.addSpacing(
            32
        )