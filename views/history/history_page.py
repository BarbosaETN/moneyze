from datetime import (
    date,
    timedelta,
)

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
)

from components.containers.history_grid import (
    HistoryGrid,
)

from components.filters.history_filters import HistoryFilters

from components.empty_state import (
    EmptyState,
)

from database.connection import get_session

from enums.transaction_type import (
    TransactionType,
)

from repositories.transaction_repository import (
    TransactionRepository,
)

from services.history_service import (
    HistoryService,
)

from views.base.base_page import BasePage


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
        self._create_headers()
        self._create_history_grid()

    def _create_filters(self):

        self.history_filters = (
            HistoryFilters()
        )

        self.content_layout.addWidget(
            self.history_filters
        )

    def _create_headers(self):

        self.headers_widget = QLabel()

        headers_layout = QHBoxLayout()

        headers_layout.setContentsMargins(
            28,
            0,
            28,
            0,
        )

        headers_layout.setSpacing(
            20
        )

        self.headers_widget.setLayout(
            headers_layout
        )

        self._create_header(
            headers_layout,
            "DATA",
            2,
            Qt.AlignmentFlag.AlignLeft,
        )

        self._create_header(
            headers_layout,
            "DESCRIÇÃO",
            4,
            Qt.AlignmentFlag.AlignLeft,
        )

        self._create_header(
            headers_layout,
            "CATEGORIA",
            2,
            Qt.AlignmentFlag.AlignCenter,
        )

        self._create_header(
            headers_layout,
            "VALOR",
            2,
            Qt.AlignmentFlag.AlignCenter,
        )

        self.content_layout.addWidget(
            self.headers_widget
        )

    def _create_header(
        self,
        layout,
        text,
        stretch,
        alignment,
    ):

        label = QLabel(
            text
        )

        label.setObjectName(
            "historyHeader"
        )

        label.setAlignment(
            alignment
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            label,
            stretch,
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
            self.history_grid,
            1,
        )

        self.content_layout.addWidget(
            self.empty_state,
            1,
        )

    def _connect_signals(self):

        self.history_filters.filters_changed.connect(
            self._on_filters_changed
        )

    def _on_filters_changed(self):

        self.load_transactions()

    def load_transactions(self):

        selected_type = (
            self.history_filters.type_filter.currentText()
        )

        transaction_type = (
            self._get_transaction_type(
                selected_type
            )
        )

        start_date, end_date = (
            self._get_period_dates()
        )

        search_text = (
            self.history_filters.search_input.text()
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

        transaction_data = (
            self._format_transactions(
                transactions
            )
        )

        self.history_grid.set_transactions(
            transaction_data
        )

    def _get_transaction_type(
        self,
        selected_type: str,
    ):

        if selected_type == "Receitas":

            return TransactionType.INCOME

        if selected_type == "Despesas":

            return TransactionType.EXPENSE

        return None

    def _get_period_dates(self):

        selected_period = (
            self.history_filters
            .period_filter
            .currentText()
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
                today.replace(
                    day=1
                )
            )

            end_date = (
                first_day_current_month
                - timedelta(
                    days=1
                )
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

        return len(
            transactions
        ) > 0

    def _update_empty_state(
        self,
        transactions,
    ):

        if transactions:

            self.headers_widget.show()
            self.history_grid.show()
            self.empty_state.hide()

            return

        self.headers_widget.hide()
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

    def _format_transactions(
        self,
        transactions,
    ):

        transaction_data = []

        for transaction in transactions:

            transaction_data.append(
                {
                    "title": (
                        transaction.description
                    ),
                    "amount": (
                        transaction.amount
                    ),
                    "category_name": (
                        transaction.category.name
                        if transaction.category
                        is not None
                        else "Sem categoria"
                    ),
                    "transaction_date": (
                        transaction
                        .transaction_date
                        .strftime(
                            "%d/%m/%Y"
                        )
                    ),
                    "transaction_type": (
                        transaction
                        .transaction_type
                    ),
                }
            )

        return transaction_data