from datetime import date

from components.containers.balance_evolution_section import (
    BalanceEvolutionSection,
)

from components.containers.category_distribution_section import (
    CategoryDistributionSection,
)

from core.data_events import (
    data_events,
)

from components.containers.monthly_comparison_section import (
    MonthlyComparisonSection,
)

from database.connection import (
    get_session,
)

from PySide6.QtWidgets import QScrollArea

from repositories.transaction_repository import (
    TransactionRepository,
)

from services.report_service import (
    ReportService,
)

from views.base.base_page import (
    BasePage,
)


class ReportPage(BasePage):

    def __init__(self):

        super().__init__(
            "Relatórios",
            "Análises e informações sobre suas finanças.",
        )

        self._setup_scroll()

        self._create_services()

        self._setup_page()

        self._connect_signals()

    def _setup_scroll(self):

        self.main_layout.removeWidget(
            self.content
        )

        self.scroll_area = QScrollArea()

        self.scroll_area.setObjectName(
            "reportScrollArea"
        )

        self.scroll_area.setWidgetResizable(
            True
        )

        self.scroll_area.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        self.scroll_area.setWidget(
            self.content
        )

        self.main_layout.addWidget(
            self.scroll_area,
            1,
        )    

    def _create_services(self):

        self.session = get_session()

        transaction_repository = (
            TransactionRepository(
                self.session
            )
        )

        self.report_service = (
            ReportService(
                transaction_repository
            )
        )

    def _setup_page(self):

        self._create_monthly_comparison()

        self._create_category_distribution()

        self._create_balance_evolution()

        self._load_monthly_comparison()

        self._load_category_distribution()

        self._load_balance_evolution()

    def _create_monthly_comparison(self):

        self.monthly_comparison_section = (
            MonthlyComparisonSection()
        )

        self.content_layout.addWidget(
            self.monthly_comparison_section
        )

    def _load_category_distribution(self):

        current_year = (
            date.today().year
        )

        category_data = (
            self.report_service
            .get_expense_distribution_by_category(
                current_year
            )
        )

        self.category_distribution_section.set_category_data(
            category_data
        )    

    def _create_category_distribution(self):

        self.category_distribution_section = (
            CategoryDistributionSection()
        )

        self.content_layout.addWidget(
            self.category_distribution_section
        )

    def _create_balance_evolution(self):

        self.balance_evolution_section = (
            BalanceEvolutionSection()
        )

        self.content_layout.addWidget(
            self.balance_evolution_section
        )

    def _load_balance_evolution(self):

        current_year = (
            date.today().year
        )

        balance_data = (
            self.report_service
            .get_balance_evolution(
                current_year
            )
        )

        self.balance_evolution_section.set_balance_data(
            balance_data
        )           

    def _load_monthly_comparison(self):

        current_year = (
            date.today().year
        )

        monthly_data = (
            self.report_service
            .get_income_expense_by_month(
                current_year
            )
        )

        self.monthly_comparison_section.set_monthly_data(
            monthly_data
        )

    def closeEvent(
        self,
        event,
    ):

        self.session.close()

        event.accept()

    def _connect_signals(self):

        data_events.transactions_changed.connect(
            self.refresh
        )

    def refresh(self):

        self._load_monthly_comparison()

        self._load_category_distribution()

        self._load_balance_evolution()