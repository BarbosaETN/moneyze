from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
)

from components.buttons.primary_button import PrimaryButton
from components.containers.category_grid import CategoryGrid
from components.dialogs.category_dialog import CategoryDialog
from data.demo.category_demo import DEMO_CATEGORIES
from views.base.base_page import BasePage


class CategoryPage(BasePage):

    def __init__(self):
        super().__init__(
            "Categorias",
            "Gerencie suas categorias financeiras."
        )

        self._setup_page()
        self._connect_signals()
        self.load_categories()

    def _setup_page(self):

        self._create_toolbar()
        self._create_grid()

    def _create_toolbar(self):

        self.toolbar = QWidget()

        self.toolbar_layout = QHBoxLayout(self.toolbar)
        self.toolbar_layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar_layout.addStretch()

        self.new_category_button = PrimaryButton(
            "+ Nova Categoria"
        )

        self.toolbar_layout.addWidget(
            self.new_category_button,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        self.content_layout.addWidget(self.toolbar)

    def _create_grid(self):

        self.category_grid = CategoryGrid()

        self.content_layout.addWidget(self.category_grid)

    def load_categories(self):

        categories= self.category_service.get_all()
        self.category_grid.set_categories(categories)

    def _connect_signals(self):

        self.new_category_button.clicked.connect(
            self._open_category_dialog
        )

    def _open_category_dialog(self):

        dialog = CategoryDialog()

        if dialog.exec():

            data = dialog.get_data()

            print(data)