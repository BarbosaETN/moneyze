from calendar import monthrange
from datetime import date

from PySide6.QtWidgets import (
    QMessageBox,
)

from components.cards.summary_card import (
    SummaryCard,
)

from core.data_events import (
    data_events,
)

from components.containers.expense_grid import (
    ExpenseGrid,
)

from components.containers.transaction_header import (
    TransactionHeader,
)

from components.navigation.month_selector import (
    MonthSelector,
)

from components.dialogs.expense_dialog import (
    ExpenseDialog,
)

from database.connection import (
    get_session,
)

from enums.transaction_type import (
    TransactionType,
)

from exceptions.moneyze_error import (
    MoneyzeError,
)

from repositories.category_repository import (
    CategoryRepository,
)

from repositories.transaction_repository import (
    TransactionRepository,
)

from services.category_service import (
    CategoryService,
)

from services.transaction_service import (
    TransactionService,
)

from views.base.base_page import (
    BasePage,
)


class ExpensePage(BasePage):

    def __init__(self):

        super().__init__(
            "Despesas",
            "Acompanhe e gerencie suas despesas.",
        )

        self._create_services()

        today = date.today()

        self.selected_year = today.year
        self.selected_month = today.month

        self._setup_page()
        self._connect_signals()

        self.load_expenses()

    def _create_services(self):

        self.session = get_session()

        transaction_repository = (
            TransactionRepository(
                self.session
            )
        )

        category_repository = (
            CategoryRepository(
                self.session
            )
        )

        self.transaction_service = (
            TransactionService(
                transaction_repository
            )
        )

        self.category_service = (
            CategoryService(
                category_repository,
                transaction_repository,
            )
        )

    def _setup_page(self):

        self._create_month_selector()
        self._create_summary()
        self._create_transaction_header()
        self._create_grid()

    def _create_month_selector(self):

        self.month_selector = (
            MonthSelector()
        )

        self._update_month_label()

        self.content_layout.addWidget(
            self.month_selector
        )

    def _create_summary(self):

        self.expense_summary = SummaryCard(
            title="Total de Despesas",
            amount=0,
            icon_name="fa5s.arrow-down",
            icon_color="#F87171",
            icon_background="#3D2028",
            amount_color="#F87171",
            button_text="Nova Despesa",
            button_icon="fa5s.plus",
        )

        self.content_layout.addWidget(
            self.expense_summary
        )

    def _create_transaction_header(self):

        self.transaction_header = (
            TransactionHeader()
        )

        self.content_layout.addWidget(
            self.transaction_header
        )

    def _create_grid(self):

        self.expense_grid = ExpenseGrid()

        self.content_layout.addWidget(
            self.expense_grid
        )

    def _connect_signals(self):

        self.expense_summary.action_requested.connect(
            self._open_expense_dialog
        )

        self.expense_grid.delete_requested.connect(
            self._delete_expense
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

        self.load_expenses()

    def _go_to_next_month(self):

        self.selected_month += 1

        if self.selected_month == 13:

            self.selected_month = 1
            self.selected_year += 1

        self._update_month_label()

        self.load_expenses()

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

    def load_expenses(self):

        start_date, end_date = (
            self._get_selected_month_range()
        )

        expenses = (
            self.transaction_service
            .get_expenses(
                start_date=start_date,
                end_date=end_date,
            )
        )

        total_expenses = sum(
            expense.amount
            for expense in expenses
        )

        self.expense_summary.update_amount(
            total_expenses
        )

        expense_data = []

        for expense in expenses:

            expense_data.append(
                {
                    "id": expense.id,
                    "title": expense.title,
                    "amount": expense.amount,
                    "transaction_date": (
                        expense.transaction_date
                        .strftime(
                            "%d/%m/%Y"
                        )
                    ),
                    "category_name": (
                        expense.category.name
                        if expense.category
                        else "Sem categoria"
                    ),
                }
            )

        self.expense_grid.set_expenses(
            expense_data
        )

    def _open_expense_dialog(self):

        categories = (
            self.category_service
            .get_all()
        )

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
                (
                    "Crie uma categoria antes de "
                    "adicionar uma despesa."
                ),
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

            data_events.transactions_changed.emit()

            self.load_expenses()

            QMessageBox.information(
                self,
                "Despesa criada",
                (
                    "A despesa foi criada "
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
                    "ao criar a despesa."
                ),
            )

    def _delete_expense(
        self,
        transaction_id: int,
    ):

        reply = QMessageBox.question(
            self,
            "Excluir despesa",
            "Deseja realmente excluir esta despesa?",
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

            data_events.transactions_changed.emit()

            self.load_expenses()

            QMessageBox.information(
                self,
                "Despesa excluída",
                (
                    "A despesa foi excluída "
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
                    "ao excluir a despesa."
                ),
            )

    def closeEvent(
        self,
        event,
    ):

        self.session.close()

        event.accept()