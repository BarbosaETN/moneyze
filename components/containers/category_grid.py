from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from components.cards.category_card import CategoryCard


class CategoryGrid(QScrollArea):

    delete_requested = Signal(int)

    def __init__(self):
        super().__init__()

        self.setObjectName("categoryGrid")

        self._setup_ui()

    def _setup_ui(self):

        self.setWidgetResizable(True)

        self.container = QWidget()

        self.container.setObjectName(
            "categoryGridContainer"
        )

        self.main_layout = QVBoxLayout(
            self.container
        )

        self.main_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.main_layout.setSpacing(0)

        self._create_grid()

        self._create_empty_state()

        self.setWidget(
            self.container
        )

    def _create_grid(self):

        self.grid_widget = QWidget()

        self.grid_layout = QGridLayout(
            self.grid_widget
        )

        self.grid_layout.setSpacing(20)

        self.grid_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.main_layout.addWidget(
            self.grid_widget
        )

    def _create_empty_state(self):

        self.empty_widget = QWidget()

        empty_layout = QVBoxLayout(
            self.empty_widget
        )

        empty_layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title = QLabel(
            "Nenhuma categoria cadastrada"
        )

        title.setObjectName(
            "categoryEmptyTitle"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        description = QLabel(
            "Crie categorias para organizar\n"
            "suas receitas e despesas."
        )

        description.setObjectName(
            "categoryEmptyDescription"
        )

        description.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        empty_layout.addStretch()

        empty_layout.addWidget(
            title
        )

        empty_layout.addWidget(
            description
        )

        empty_layout.addStretch()

        self.main_layout.addWidget(
            self.empty_widget
        )

        self.empty_widget.hide()

    def set_categories(
        self,
        categories,
    ):

        self._clear()

        if not categories:

            self.grid_widget.hide()

            self.empty_widget.show()

            return

        self.empty_widget.hide()

        self.grid_widget.show()

        columns = 2

        for index, category in enumerate(
            categories
        ):

            row = index // columns

            column = index % columns

            card = CategoryCard(
                category_id=category["id"],
                name=category["name"],
                budget=category["budget"],
                spent=category["spent"],
                remaining=category["remaining"],
                percentage=category["percentage"],
            )

            card.delete_requested.connect(
                self._on_delete_requested
            )

            self.grid_layout.addWidget(
                card,
                row,
                column,
            )

    def _clear(self):

        while self.grid_layout.count():

            item = self.grid_layout.takeAt(
                0
            )

            if item.widget():

                item.widget().deleteLater()

    def _on_delete_requested(
        self,
        category_id: int,
    ):

        self.delete_requested.emit(
            category_id
        )