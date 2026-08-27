from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMessageBox,
    QWidget,
    QPushButton,
    QLabel
)

from components.buttons.primary_button import PrimaryButton
from components.containers.category_grid import CategoryGrid
from components.dialogs.category_dialog import CategoryDialog

from database.connection import get_session

from exceptions.moneyze_error import MoneyzeError

from repositories.category_repository import CategoryRepository
from repositories.transaction_repository import (
    TransactionRepository,
)

from services.category_service import CategoryService

from views.base.base_page import BasePage

from calendar import monthrange
from datetime import date


class CategoryPage(BasePage):

    def __init__(self):
        super().__init__(
            "Categorias",
            "Gerencie suas categorias financeiras.",
        )

        self.session = get_session()

        category_repository = CategoryRepository(
            self.session
        )

        transaction_repository = TransactionRepository(
            self.session
        )

        self.category_service = CategoryService(
            category_repository,
            transaction_repository,
        )

        today = date.today()

        self.selected_year = today.year
        self.selected_month = today.month

        self._setup_page()
        self._connect_signals()
        self.load_categories()

    def _setup_page(self):

        self._create_month_selector()
        self._create_toolbar()
        self._create_grid()

    def _create_toolbar(self):

        self.toolbar = QWidget()

        self.toolbar_layout = QHBoxLayout(
            self.toolbar
        )

        self.toolbar_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.toolbar_layout.addStretch()

        self.new_category_button = PrimaryButton(
            "+ Nova Categoria"
        )

        self.toolbar_layout.addWidget(
            self.new_category_button,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

        self.content_layout.addWidget(
            self.toolbar
        )

    def _create_grid(self):

        self.category_grid = CategoryGrid()

        self.content_layout.addWidget(
            self.category_grid
        )

    def _create_month_selector(self):

        self.month_selector = QWidget()

        self.month_selector_layout = QHBoxLayout(
            self.month_selector
        )

        self.month_selector_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.previous_month_button = QPushButton(
            "<"
        )

        self.previous_month_button.setObjectName(
            "monthNavigationButton"
        )

        self.month_label = QLabel()

        self.month_label.setObjectName(
            "monthLabel"
        )

        self.month_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.next_month_button = QPushButton(
            ">"
        )

        self.next_month_button.setObjectName(
            "monthNavigationButton"
        )

        self.month_selector_layout.addStretch()

        self.month_selector_layout.addWidget(
            self.previous_month_button
        )

        self.month_selector_layout.addWidget(
            self.month_label
        )

        self.month_selector_layout.addWidget(
            self.next_month_button
        )

        self.month_selector_layout.addStretch()

        self._update_month_label()

        self.content_layout.addWidget(
            self.month_selector
        )    

    def _update_month_label(self):

        months = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]

        month_name = months[
            self.selected_month - 1
        ]

        self.month_label.setText(
            f"{month_name} {self.selected_year}"
        )    

    def load_categories(self):

        start_date, end_date = (
            self._get_selected_month_range()
        )

        categories = (
            self.category_service
            .get_categories_with_summary(
                start_date=start_date,
                end_date=end_date,
            )
        )

        self.category_grid.set_categories(
            categories
        )

    def _connect_signals(self):

        self.new_category_button.clicked.connect(
            self.open_create_dialog
        )

        self.category_grid.delete_requested.connect(
            self._delete_category
        )

        self.previous_month_button.clicked.connect(
            self._go_to_previous_month
        )

        self.next_month_button.clicked.connect(
            self._go_to_next_month
        )

    def _go_to_previous_month(self):

        self.selected_month -= 1

        if self.selected_month == 0:

            self.selected_month = 12
            self.selected_year -= 1

        self._update_month_label()

        self.load_categories() 

    def _go_to_next_month(self):

        self.selected_month += 1

        if self.selected_month == 13:

            self.selected_month = 1
            self.selected_year += 1

        self._update_month_label()

        self.load_categories()       

    def open_create_dialog(self):

        dialog = CategoryDialog()

        if not dialog.exec():
            return

        data = dialog.get_data()

        try:

            self.category_service.create(
                name=data["name"],
                budget=data["budget"],
            )

            self.load_categories()

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                error.title,
                error.message,
            )

    def _delete_category(
        self,
        category_id: int,
    ):

        reply = QMessageBox.question(
            self,
            "Excluir categoria",
            "Deseja realmente excluir esta categoria?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.No:
            return

        try:

            self.category_service.delete_by_id(
                category_id
            )

            self.load_categories()

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                error.title,
                error.message,
            )

    def _get_selected_month_range(self):

        start_date = date(
            self.selected_year,
            self.selected_month,
            1,
        )

        last_day = monthrange(
            self.selected_year,
            self.selected_month,
        )[1]

        end_date = date(
            self.selected_year,
            self.selected_month,
            last_day,
        )

        return start_date, end_date        