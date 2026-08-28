from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QScrollArea,
    QWidget,
)

from components.cards.income_card import IncomeCard


class IncomeGrid(QScrollArea):

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

        self.setWidgetResizable(
            True
        )

        self._setup_ui()

    def _setup_ui(self):

        self.setObjectName(
            "incomeGrid"
        )

        self.container.setObjectName(
            "incomeGridContainer"
        )

        self.setFrameShape(
            QFrame.Shape.NoFrame
        )

        self.setLineWidth(
            0
        )

        self.setMidLineWidth(
            0
        )

        self.grid_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.grid_layout.setSpacing(
            0
        )

        self.grid_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

    def set_incomes(
        self,
        incomes,
    ):

        self._clear_grid()

        columns = 1

        for index, income in enumerate(
            incomes
        ):

            row = index // columns
            column = index % columns

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

            self.grid_layout.addWidget(
                card,
                row,
                column,
                alignment=Qt.AlignmentFlag.AlignTop,
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

            item = self.grid_layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()