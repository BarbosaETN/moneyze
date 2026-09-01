from datetime import date

from components.containers.balance_evolution_section import (
    BalanceEvolutionSection,
)

from components.containers.category_distribution_section import (
    CategoryDistributionSection,
)

from components.containers.monthly_comparison_section import (
    MonthlyComparisonSection,
)

from database.connection import (
    get_session,
)

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

        self._create_services()

        self._setup_page()

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