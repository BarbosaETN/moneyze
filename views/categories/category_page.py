from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QMessageBox
)

from exceptions.moneyze_error import MoneyzeError
from database.connection import get_session
from repositories.category_repository import CategoryRepository
from services.category_service import CategoryService
from components.buttons.primary_button import PrimaryButton
from components.containers.category_grid import CategoryGrid
from components.dialogs.category_dialog import CategoryDialog
from views.base.base_page import BasePage


class CategoryPage(BasePage):

    def __init__(self):
        super().__init__(
            "Categorias",
            "Gerencie suas categorias financeiras."
        )
        self.session = get_session()
        repository = CategoryRepository(self.session)
        self.category_service = CategoryService(repository)

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

        cards = []

        for category in categories:

            cards.append({

                "id": category.id,

                "name": category.name,

                "budget": 0,

                "spent": 0,

            })    

        self.category_grid.set_categories(cards)

    def _connect_signals(self):

        self.new_category_button.clicked.connect(
            self._open_category_dialog
        )

        self.category_grid.delete_requested.connect(
            self._delete_category
        )

    def _open_category_dialog(self):

        dialog = CategoryDialog()

        if dialog.exec():

            try:
                data = dialog.get_data()

                self.category_service.create(**data)
                self.load_categories()
            except Exception as error:
                print(error)


    def _delete_category(self, category_id: int):

        reply = QMessageBox.question(
            self,
            "Exluir categoria",
            "Deseja realmente excluir esta categoria?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.No:
            return

        try:

            self.category_service.delete_by_id(category_id)

            self.load_categories()

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                error.title,
                error.message,
            )