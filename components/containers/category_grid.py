from PySide6.QtWidgets import (
    QGridLayout,
    QScrollArea,
    QWidget,
)

from components.cards.category_card import CategoryCard


class CategoryGrid(QScrollArea):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        self.setWidgetResizable(True)

        self.container = QWidget()

        self.grid_layout = QGridLayout(self.container)
        self.grid_layout.setSpacing(20)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.setWidget(self.container)

    def set_categories(self, categories):

        self._clear()

        columns = 3

        for index, category in enumerate(categories):

            row = index // columns
            column = index % columns

            card = CategoryCard(
                name=category["name"],
                budget=category["budget"],
                spent=category["spent"],
            )

            self.grid_layout.addWidget(card, row, column)

    def _clear(self):

        while self.grid_layout.count():

            item = self.grid_layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()