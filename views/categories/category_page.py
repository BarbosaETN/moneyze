from calendar import monthrange
from datetime import date

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMessageBox,
    QWidget,
)

from components.buttons.primary_button import PrimaryButton
from components.containers.category_grid import CategoryGrid
from components.dialogs.category_dialog import CategoryDialog
from components.navigation.month_selector import MonthSelector

from database.connection import get_session

from core.data_events import (
    data_events,
)

from exceptions.moneyze_error import MoneyzeError

from repositories.category_repository import (
    CategoryRepository,
)

from repositories.transaction_repository import (
    TransactionRepository,
)

from services.category_service import CategoryService

from views.base.base_page import BasePage


class CategoryPage(BasePage):

    def __init__(self):

        super().__init__(
            "Categorias",
            "Gerencie suas categorias financeiras.",
        )

        self.session = get_session()

        self._create_services()

        today = date.today()

        self.selected_year = today.year
        self.selected_month = today.month

        self._setup_page()
        self._connect_signals()

        data_events.transactions_changed.connect(
            self.refresh
        )

        self._update_month_label()
        self.load_categories()

    def _create_services(self):

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

    def _setup_page(self):

        self._create_month_selector()
        self._create_toolbar()
        self._create_grid()

    def _create_month_selector(self):

        self.month_selector = MonthSelector()

        self.content_layout.addWidget(
            self.month_selector
        )

    def _create_toolbar(self):

        self.toolbar = QWidget()

        self.toolbar.setObjectName(
            "categoryToolbar"
        )

        self.toolbar_layout = QHBoxLayout(
            self.toolbar
        )

        self.toolbar_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.new_category_button = PrimaryButton(
            "Nova Categoria",
            "fa5s.plus",
        )

        self.toolbar_layout.addStretch()

        self.toolbar_layout.addWidget(
            self.new_category_button
        )

        self.content_layout.addWidget(
            self.toolbar
        )

    def _create_grid(self):

        self.category_grid = CategoryGrid()

        self.content_layout.addWidget(
            self.category_grid
        )

    def _connect_signals(self):

        self.new_category_button.clicked.connect(
            self.open_create_dialog
        )

        self.category_grid.create_requested.connect(
            self.open_create_dialog
        )

        self.category_grid.delete_requested.connect(
            self._delete_category
        )

        self.month_selector.previous_requested.connect(
            self._go_to_previous_month
        )

        self.month_selector.next_requested.connect(
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

        self.month_selector.set_month_text(
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

        return (
            start_date,
            end_date,
        )

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
            QMessageBox.Yes
            | QMessageBox.No,
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

    def refresh(self):

        self.load_categories()        