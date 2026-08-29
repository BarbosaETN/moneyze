from PySide6.QtWidgets import (
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from components.cards.history_card import (
    HistoryCard,
)


class HistoryGrid(QScrollArea):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "historyGrid"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.setWidgetResizable(
            True
        )

        self._create_container()

        self.setWidget(
            self.container
        )

    def _create_container(self):

        self.container = QWidget()

        self.container.setObjectName(
            "historyGridContainer"
        )

        self.layout = QVBoxLayout(
            self.container
        )

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.layout.setSpacing(
            0
        )

    def set_transactions(
        self,
        transactions,
    ):

        self._clear()

        for transaction in transactions:

            card = HistoryCard(
                title=transaction["title"],
                amount=transaction["amount"],
                category_name=(
                    transaction[
                        "category_name"
                    ]
                ),
                transaction_date=(
                    transaction[
                        "transaction_date"
                    ]
                ),
                transaction_type=(
                    transaction[
                        "transaction_type"
                    ]
                ),
            )

            self.layout.addWidget(
                card
            )

        self.layout.addStretch()

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()