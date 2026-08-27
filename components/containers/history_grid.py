from PySide6.QtWidgets import (
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from components.cards.history_card import HistoryCard


class HistoryGrid(QScrollArea):

    def __init__(self):
        super().__init__()

        self.container = QWidget()

        self.layout = QVBoxLayout(
            self.container
        )

        self.setWidget(
            self.container
        )

        self.setWidgetResizable(True)

        self._setup_ui()

    def _setup_ui(self):

        self.layout.setSpacing(8)

    def set_transactions(self, transactions):

        self._clear()

        for transaction in transactions:

            card = HistoryCard(
                title=transaction["title"],
                amount=transaction["amount"],
                category_name=transaction[
                    "category_name"
                ],
                transaction_date=transaction[
                    "transaction_date"
                ],
                transaction_type=transaction[
                    "transaction_type"
                ],
            )

            self.layout.addWidget(card)

        self.layout.addStretch()

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()