from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from components.cards.income_card import IncomeCard


class IncomeGrid(QScrollArea):

    delete_requested = Signal(int)

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "incomeGrid"
        )

        self.setWidgetResizable(True)

        self.container = QWidget()

        self.container.setObjectName(
            "incomeGridContainer"
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

        self.layout.setSpacing(0)

        self.setWidget(
            self.container
        )

    def set_incomes(self, incomes):

        self._clear_grid()

        for income in incomes:

            card = IncomeCard(
                transaction_id=income["id"],
                title=income["title"],
                amount=income["amount"],
                transaction_date=income[
                    "transaction_date"
                ],
                category_name=income[
                    "category_name"
                ],
            )

            card.delete_requested.connect(
                self._on_delete_requested
            )

            self.layout.addWidget(
                card
            )

        self.layout.addStretch()

    def _on_delete_requested(
        self,
        transaction_id: int,
    ):

        self.delete_requested.emit(
            transaction_id
        )

    def _clear_grid(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()