from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QLabel,
)

from components.containers.history_grid import HistoryGrid

from database.connection import get_session

from repositories.transaction_repository import (
    TransactionRepository,
)

from services.history_service import HistoryService

from views.base.base_page import BasePage

from enums.transaction_type import TransactionType

from datetime import date, timedelta

from components.empty_state import EmptyState


class HistoryPage(BasePage):

    def __init__(self):
        super().__init__(
            "Histórico",
            "Todas as suas movimentações.",
        )

        self._create_services()

        self._setup_page()
        self._connect_signals()

        self.load_transactions()

    def _create_services(self):

        self.session = get_session()

        transaction_repository = (
            TransactionRepository(
                self.session
            )
        )

        self.history_service = HistoryService(
            transaction_repository
        )

    def _setup_page(self):

        self._create_filters()
        self._create_history_grid()

    def _create_filters(self):

        filters_layout = QHBoxLayout()

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Buscar movimentação..."
        )

        self.type_filter = QComboBox()

        self.type_filter.addItem("Todos")
        self.type_filter.addItem("Receitas")
        self.type_filter.addItem("Despesas")

        self.period_filter = QComboBox()

        self.period_filter.addItem("Todos")
        self.period_filter.addItem("Este mês")
        self.period_filter.addItem("Mês passado")

        filters_layout.addWidget(
            self.search_input
        )

        filters_layout.addWidget(
            self.type_filter
        )

        filters_layout.addWidget(
            self.period_filter
        )

        self.content_layout.addLayout(
            filters_layout
        )

    def _create_history_grid(self):

        self.history_grid = HistoryGrid()

        self.empty_state = EmptyState(
            title="Nenhuma transação cadastrada",
            description=(
                "Adicione uma receita ou despesa "
                "para começar a acompanhar suas finanças."
            ),
        )

        self.empty_state.hide()

        self.content_layout.addWidget(
            self.history_grid
        )

        self.content_layout.addWidget(
            self.empty_state
        )

    def _connect_signals(self):

        self.search_input.textChanged.connect(
            self._on_filters_changed
        )

        self.type_filter.currentIndexChanged.connect(
            self._on_filters_changed
        )

        self.period_filter.currentIndexChanged.connect(
            self._on_filters_changed
        )

    def _on_filters_changed(self):

        self.load_transactions()

    def load_transactions(self):

        selected_type = (
            self.type_filter.currentText()
        )

        transaction_type = None

        if selected_type == "Receitas":

            transaction_type = (
                TransactionType.INCOME
            )

        elif selected_type == "Despesas":

            transaction_type = (
                TransactionType.EXPENSE
            )

        start_date, end_date = (
            self._get_period_dates()
        )

        search_text = (
            self.search_input.text()
        )

        transactions = (
            self.history_service.get_transactions(
                transaction_type=transaction_type,
                start_date=start_date,
                end_date=end_date,
                search_text=search_text,
            )
        )

        self._update_empty_state(
            transactions
        )

        if not transactions:
            return

        transaction_data = []

        for transaction in transactions:

            transaction_data.append(
                {
                    "title": transaction.description,
                    "amount": transaction.amount,
                    "category_name": (
                        transaction.category.name
                        if transaction.category is not None
                        else "Sem categoria"
                    ),
                    "transaction_date": (
                        transaction.transaction_date.strftime(
                            "%d/%m/%Y"
                        )
                    ),
                    "transaction_type": (
                        transaction.transaction_type
                    ),
                }
            )

        self.history_grid.set_transactions(
            transaction_data
        )

    def _get_period_dates(self):

        selected_period = (
            self.period_filter.currentText()
        )

        today = date.today()

        if selected_period == "Este mês":

            start_date = today.replace(
                day=1
            )

            end_date = today

            return (
                start_date,
                end_date,
            )

        if selected_period == "Mês passado":

            first_day_current_month = (
                today.replace(day=1)
            )

            end_date = (
                first_day_current_month
                - timedelta(days=1)
            )

            start_date = end_date.replace(
                day=1
            )

            return (
                start_date,
                end_date,
            )

        return (
            None,
            None,
        )

    def _has_transactions(self):

        transactions = (
            self.history_service.get_all()
        )

        return len(transactions) > 0

    def _update_empty_state(
        self,
        transactions,
    ):

        if transactions:

            self.history_grid.show()
            self.empty_state.hide()

            return

        self.history_grid.hide()

        has_transactions = (
            self._has_transactions()
        )

        if has_transactions:

            self.empty_state.set_content(
                title=(
                    "Nenhuma transação encontrada"
                ),
                description=(
                    "Nenhuma transação encontrada "
                    "para os filtros selecionados."
                ),
            )

        else:

            self.empty_state.set_content(
                title=(
                    "Nenhuma transação cadastrada"
                ),
                description=(
                    "Adicione uma receita ou despesa "
                    "para começar a acompanhar suas finanças."
                ),
            )

        self.empty_state.show()

    def _refresh_empty_state(self):

        title_label = (
            self.empty_state.findChild(
                QLabel,
                "emptyStateTitle",
            )
        )

        description_label = (
            self.empty_state.findChild(
                QLabel,
                "emptyStateDescription",
            )
        )

        title_label.setText(
            self.empty_state.title
        )

        description_label.setText(
            self.empty_state.description
        )