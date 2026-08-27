from PySide6.QtWidgets import (
    QHBoxLayout,
    QMessageBox,
)

from components.buttons.primary_button import PrimaryButton
from components.containers.income_grid import IncomeGrid
from components.dialogs.income_dialog import IncomeDialog

from database.connection import get_session

from enums.transaction_type import TransactionType

from components.containers.income_header import (
    IncomeHeader,
)

from exceptions.moneyze_error import MoneyzeError

from components.cards.summary_card import SummaryCard

from repositories.transaction_repository import (
    TransactionRepository,
)

from services.transaction_service import (
    TransactionService,
)

from views.base.base_page import BasePage


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

        self._create_summary()
        self._create_grid()

    def _create_services(self):

        self.session = get_session()

        transaction_repository = (
            TransactionRepository(
                self.session
            )
        )

        self.transaction_service = (
            TransactionService(
                transaction_repository
            )
        )

    def _create_toolbar(self):

        self.toolbar_layout = (
            QHBoxLayout()
        )

        self.toolbar_layout.addStretch()

        self.new_income_button = (
            PrimaryButton(
                "Nova Receita"
            )
        )

        self.toolbar_layout.addWidget(
            self.new_income_button
        )

        self.content_layout.addLayout(
            self.toolbar_layout
        )

    def _create_summary(self):

        self.income_summary = SummaryCard(
            title="Total de Receitas",
            amount=0,
            icon_name="fa5s.arrow-up",
            icon_color="#34D399",
            icon_background="#123D35",
            button_text="Nova Receita",
            button_icon="fa5s.plus",
        )

        self.content_layout.addWidget(
            self.income_summary
        )    

    def _create_grid(self):

        self.income_header = IncomeHeader()

        self.income_grid = IncomeGrid()

        self.content_layout.addWidget(
            self.income_header
        )

        self.content_layout.addWidget(
            self.income_grid
        )

    def _connect_signals(self):

        self.income_summary.action_requested.connect(
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

        total_income = sum(
            income.amount
            for income in incomes
        )

        self.income_summary.update_amount(
            total_income
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
                    if income.category
                    else "Receita"
                ),
            })

        self.income_grid.set_incomes(
            income_data
        )

    def _open_income_dialog(self):

        dialog = IncomeDialog()

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
                error.title,
                error.message,
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Erro inesperado",
                (
                    "Ocorreu um erro inesperado "
                    "ao criar a receita."
                ),
            )

    def _delete_income(
        self,
        transaction_id: int,
    ):

        reply = QMessageBox.question(
            self,
            "Excluir receita",
            "Deseja realmente excluir esta receita?",
            QMessageBox.Yes
            | QMessageBox.No,
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
                (
                    "A receita foi excluída "
                    "com sucesso."
                ),
            )

        except MoneyzeError as error:

            QMessageBox.warning(
                self,
                error.title,
                error.message,
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Erro inesperado",
                (
                    "Ocorreu um erro inesperado "
                    "ao excluir a receita."
                ),
            )

    def closeEvent(self, event):

        self.session.close()

        event.accept()