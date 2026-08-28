from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QWidget,
)


class TransactionHeader(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "transactionHeader"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            28,
            0,
            28,
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

        description_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        category_label = QLabel(
            "CATEGORIA"
        )

        category_label.setObjectName(
            "transactionHeaderLabel"
        )

        category_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        amount_label = QLabel(
            "VALOR"
        )

        amount_label.setObjectName(
            "transactionHeaderLabel"
        )

        amount_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        delete_placeholder = QWidget()

        delete_placeholder.setFixedWidth(
            44
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

        layout.addWidget(
            delete_placeholder
        )