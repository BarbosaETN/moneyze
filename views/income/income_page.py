from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
)

from components.containers.income_grid import IncomeGrid
from views.base.base_page import BasePage

from database.connection import get_session
from enums.transaction_type import TransactionType

from repositories.category_repository import CategoryRepository
from repositories.transaction_repository import TransactionRepository

from services.category_service import CategoryService
from services.transaction_service import TransactionService

from components.dialogs.income_dialog import IncomeDialog

from PySide6.QtWidgets import QMessageBox

from exceptions.moneyze_error import MoneyzeError

class IncomePage(BasePage):

    def __init__(self):
        super().__init__(
            "Receitas",
            "Acompanhe e gerencie suas receitas.",
        )

        self._create_services()

        self._setup_page()
        self._connect_signals()

        self.load_incomes()

    def _setup_page(self):

        self._create_toolbar()
        self._create_grid()

    def _create_services(self):

        self.session = get_session()

        transaction_repository = TransactionRepository(
            self.session
        )

        category_repository = CategoryRepository(
            self.session
        )

        self.transaction_service = TransactionService(
            transaction_repository,
            category_repository,
        )

        self.category_service = CategoryService(
            category_repository
        )

    def _create_toolbar(self):

        self.toolbar_layout = QHBoxLayout()

        self.new_income_button = QPushButton(
            "+ Nova Receita"
        )

        self.new_income_button.setObjectName(
            "primaryButton"
        )

        self.toolbar_layout.addStretch()

        self.toolbar_layout.addWidget(
            self.new_income_button
        )

        self.content_layout.addLayout(
            self.toolbar_layout
        )

    def _create_grid(self):

        self.income_grid = IncomeGrid()

        self.content_layout.addWidget(
            self.income_grid
        )

    def _connect_signals(self):

        self.new_income_button.clicked.connect(
            self._open_income_dialog
        )

        self.income_grid.delete_requested.connect(
            self._delete_income
        )

    def load_incomes(self):

        incomes = (
            self.transaction_service
            .get_incomes()
        )

        income_data = []

        for income in incomes:

            income_data.append({
                "id": income.id,
                "title": income.title,
                "amount": income.amount,
                "transaction_date": (
                    income.transaction_date
                    .strftime("%d/%m/%Y")
                ),
                "category_name": (
                    income.category.name
                ),
            })

        self.income_grid.set_incomes(
            income_data
        )

    def closeEvent(self, event):

        self.session.close()

        event.accept()

    def _open_income_dialog(self):

        categories = self.category_service.get_all()

        category_data = [
            {
                "id": category.id,
                "name": category.name,
            }
            for category in categories
        ]

        if not category_data:

            QMessageBox.information(
                self,
                "Nenhuma categoria",
                "Crie uma categoria antes de adicionar uma receita.",
            )

            return

        dialog = IncomeDialog(
            categories=category_data
        )

        if not dialog.exec():
            return

        data = dialog.get_data()

        data["transaction_type"] = (
            TransactionType.INCOME
        )

        try:

            self.transaction_service.create(
                **data
            )

            self.load_incomes()

            QMessageBox.information(
                self,
                "Receita criada",
                "A receita foi criada com sucesso.",
            )

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                "Não foi possível criar a receita",
                str(error),
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Erro inesperado",
                "Ocorreu um erro inesperado ao criar a receita.",
            )

    def _delete_income(self, transaction_id: int):

        reply = QMessageBox.question(
            self,
            "Excluir receita",
            "Deseja realmente excluir esta receita?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.No:
            return

        try:

            self.transaction_service.delete_by_id(
                transaction_id
            )

            self.load_incomes()

            QMessageBox.information(
                self,
                "Receita excluída",
                "A receita foi excluída com sucesso.",
            )

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                "Não foi possível excluir a receita",
                str(error),
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Erro inesperado",
                "Ocorreu um erro inesperado ao excluir a receita.",
            )