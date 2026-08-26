from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QGridLayout,
    QScrollArea,
    QWidget,
)

from components.cards.expense_card import ExpenseCard


class ExpenseGrid(QScrollArea):

    delete_requested = Signal(int)

    def __init__(self):
        super().__init__()

        self.container = QWidget()

        self.grid_layout = QGridLayout(
            self.container
        )

        self.setWidget(
            self.container
        )

        self.setWidgetResizable(True)

        self._setup_ui()

    def _setup_ui(self):

        self.grid_layout.setSpacing(20)

    def set_expenses(self, expenses):

        self._clear_grid()

        columns = 3

        for index, expense in enumerate(expenses):

            row = index // columns
            column = index % columns

            card = ExpenseCard(
                transaction_id=expense["id"],
                title=expense["title"],
                amount=expense["amount"],
                transaction_date=expense[
                    "transaction_date"
                ],
                category_name=expense[
                    "category_name"
                ],
            )

            card.delete_requested.connect(
                self._on_delete_requested
            )

            self.grid_layout.addWidget(
                card,
                row,
                column,
            )

    def _on_delete_requested(
        self,
        transaction_id: int,
    ):

        self.delete_requested.emit(
            transaction_id
        )

    def _clear_grid(self):

        while self.grid_layout.count():

            item = self.grid_layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()