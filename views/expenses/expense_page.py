from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
)

from components.containers.expense_grid import ExpenseGrid
from views.base.base_page import BasePage
from PySide6.QtWidgets import QMessageBox

from components.dialogs.expense_dialog import ExpenseDialog

from database.connection import get_session

from enums.transaction_type import TransactionType

from repositories.category_repository import CategoryRepository
from repositories.transaction_repository import TransactionRepository

from services.category_service import CategoryService
from services.transaction_service import TransactionService

from exceptions.moneyze_error import MoneyzeError

class ExpensePage(BasePage):

    def __init__(self):
        super().__init__(
            "Despesas",
            "Acompanhe e gerencie suas despesas.",
        )

        self._create_services()

        self._setup_page()
        self._connect_signals()

        self.load_expenses()

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
        )

        self.category_service = CategoryService(
            category_repository
        )    

    def _setup_page(self):

        self._create_toolbar()
        self._create_grid()

    def _create_toolbar(self):

        self.toolbar_layout = QHBoxLayout()

        self.new_expense_button = QPushButton(
            "+ Nova Despesa"
        )

        self.new_expense_button.setObjectName(
            "primaryButton"
        )

        self.toolbar_layout.addStretch()

        self.toolbar_layout.addWidget(
            self.new_expense_button
        )

        self.content_layout.addLayout(
            self.toolbar_layout
        )

    def _create_grid(self):

        self.expense_grid = ExpenseGrid()

        self.content_layout.addWidget(
            self.expense_grid
        )

    def _connect_signals(self):

        self.new_expense_button.clicked.connect(
            self._open_expense_dialog
        )

        self.expense_grid.delete_requested.connect(
            self._delete_expense
        )

    def load_expenses(self):

        expenses = (
            self.transaction_service
            .get_expenses()
        )

        expense_data = [
            {
                "id": expense.id,
                "title": expense.title,
                "amount": expense.amount,
                "transaction_date": (
                    expense.transaction_date.strftime(
                        "%d/%m/%Y"
                    )
                ),
                "category_name": (
                    expense.category.name
                ),
            }
            for expense in expenses
        ]

        self.expense_grid.set_expenses(
            expense_data
        )

    def closeEvent(self, event):

        self.session.close()

        event.accept()    

    def _open_expense_dialog(self):

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
                "Crie uma categoria antes de adicionar uma despesa.",
            )

            return

        dialog = ExpenseDialog(
            categories=category_data
        )

        if not dialog.exec():
            return

        data = dialog.get_data()

        data["transaction_type"] = (
            TransactionType.EXPENSE
        )

        try:

            self.transaction_service.create(
                **data
            )

            self.load_expenses()

            QMessageBox.information(
                self,
                "Despesa criada",
                "A despesa foi criada com sucesso.",
            )

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                "Não foi possível criar a despesa",
                str(error),
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Erro inesperado",
                "Ocorreu um erro inesperado ao criar a despesa.",
            )

            if dialog.exec():

                data = dialog.get_data()

                print("Dados da despesa:")
                print(data)

    def _delete_expense(self, transaction_id: int):

        reply = QMessageBox.question(
            self,
            "Excluir despesa",
            "Deseja realmente excluir esta despesa?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.No:
            return

        try:

            self.transaction_service.delete_by_id(
                transaction_id
            )

            self.load_expenses()

            QMessageBox.information(
                self,
                "Despesa excluída",
                "A despesa foi excluída com sucesso.",
            )

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                "Não foi possível excluir a despesa",
                str(error),
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Erro inesperado",
                "Ocorreu um erro inesperado ao excluir a despesa.",
            )