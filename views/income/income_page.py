from calendar import monthrange
from datetime import date

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMessageBox,
)

from PySide6.QtCore import Qt

from components.navigation.month_selector import (
    MonthSelector,
)

from components.cards.summary_card import (
    SummaryCard,
)

from components.containers.income_grid import (
    IncomeGrid,
)

from components.containers.transaction_header import (
    TransactionHeader,
)

from components.dialogs.income_dialog import (
    IncomeDialog,
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

        today = date.today()

        self.selected_year = today.year
        self.selected_month = today.month

        self._setup_page()
        self._connect_signals()

        self.load_incomes()

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

    def _setup_page(self):

        self._create_month_selector()

        self._create_summary()

        self._create_grid()

    def _create_month_selector(self):

        self.month_selector = MonthSelector()

        self.content_layout.addWidget(
            self.month_selector,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        self._update_month_label()  

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

        self.transaction_header = TransactionHeader()

        self.income_grid = IncomeGrid()

        self.content_layout.addWidget(
            self.transaction_header
        )

        self.content_layout.addWidget(
            self.income_grid
        )

    def _connect_signals(self):

        self.month_selector.previous_requested.connect(
            self._go_to_previous_month
        )

        self.month_selector.next_requested.connect(
            self._go_to_next_month
        )

        self.income_summary.action_requested.connect(
            self._open_income_dialog
        )

        self.income_grid.delete_requested.connect(
            self._delete_income
        )

    def _go_to_previous_month(self):

        self.selected_month -= 1

        if self.selected_month == 0:

            self.selected_month = 12

            self.selected_year -= 1

        self._update_month_label()

        self.load_incomes()

    def _go_to_next_month(self):

        self.selected_month += 1

        if self.selected_month == 13:

            self.selected_month = 1

            self.selected_year += 1

        self._update_month_label()

        self.load_incomes()

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

    def load_incomes(self):

        (
            start_date,
            end_date,
        ) = self._get_selected_month_range()

        incomes = (
            self.transaction_service
            .get_incomes(
                start_date=start_date,
                end_date=end_date,
            )
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
                    "Receita"
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
                (
                    "A receita foi criada "
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
            (
                "Deseja realmente excluir "
                "esta receita?"
            ),
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
                "Não foi possível criar a receita.",
                str(error),
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

    def closeEvent(
        self,
        event,
    ):

        self.session.close()

        event.accept()