from components.containers.dashboard_summary import (
    DashboardSummary,
)

from components.containers.dashboard_content import (
    DashboardContent,
)

from core.data_events import (
    data_events,
)

from components.containers.cash_flow_section import (
    CashFlowSection,
)

from components.containers.category_section import (
    CategorySection,
)

from database.connection import (
    get_session,
)

from repositories.transaction_repository import (
    TransactionRepository,
)

from repositories.category_repository import (
    CategoryRepository,
)

from services.dashboard_service import (
    DashboardService,
)

from views.base.base_page import (
    BasePage,
)


class DashboardPage(BasePage):

    def __init__(self):

        super().__init__(
            "Dashboard",
            "Acompanhe suas finanças.",
        )

        self._create_services()

        self._setup_page()

        data_events.transactions_changed.connect(
            self.refresh
        )

    def _setup_page(self):

        self._create_summary()

        self._create_dashboard_content()

        self._load_category_data()

        self._load_cash_flow_data()

    def _create_summary(self):

        self.dashboard_summary = (
            DashboardSummary()
        )

        self.content_layout.addWidget(
            self.dashboard_summary
        )

        self._load_summary_data()

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

        self.dashboard_service = (
            DashboardService(
                transaction_repository,
                category_repository,
            )
        )    

    def _create_dashboard_content(self):

        self.dashboard_content = (
            DashboardContent()
        )

        self.cash_flow_section = (
            CashFlowSection()
        )

        self.category_section = (
            CategorySection()
        )

        self.dashboard_content.add_cash_flow_section(
            self.cash_flow_section
        )

        self.dashboard_content.add_category_section(
            self.category_section
        )

        self.content_layout.addWidget(
            self.dashboard_content,
            1,
        )

    def _load_summary_data(self):

        summary = (
            self.dashboard_service
            .get_summary()
        )

        income_variation = (
            summary["income_variation"]
        )

        expense_variation = (
            summary["expense_variation"]
        )

        income_variation_text, income_variation_color = (
            self._format_variation(
                income_variation,
                "income",
            )
        )

        expense_variation_text, expense_variation_color = (
            self._format_variation(
                expense_variation,
                "expense",
            )
        )

        balance_variation_text, balance_variation_color = (
            self._format_balance_variation(
                summary["current_balance"],
                summary["previous_balance"],
            )
        )

        summary_data = [
            {
                "title": "Saldo Total",
                "amount": summary["total_balance"],
                "icon_name": "fa5s.wallet",
                "icon_color": "#34D399",
                "icon_background": "#163B35",
                "variation_text": balance_variation_text,
                "variation_color": balance_variation_color,
            },
            {
                "title": "Receitas",
                "amount": summary["total_income"],
                "icon_name": "fa5s.arrow-up",
                "icon_color": "#34D399",
                "icon_background": "#163B35",
                "variation_text": income_variation_text,
                "variation_color": income_variation_color,
            },
            {
                "title": "Despesas",
                "amount": summary["total_expense"],
                "icon_name": "fa5s.arrow-down",
                "icon_color": "#F87171",
                "icon_background": "#3B2028",
                "variation_text": expense_variation_text,
                "variation_color": expense_variation_color,
            },
            {
                "title": "Saldo Acumulado",
                "amount": summary["accumulated_balance"],
                "icon_name": "fa5s.coins",
                "icon_color": "#60A5FA",
                "icon_background": "#1E2D4A",
                "variation_text": "",
                "variation_color": "#60A5FA",
            },
        ]

        self.dashboard_summary.set_summary(
            summary_data
        )

    def _load_category_data(self):

        categories = (
            self.dashboard_service
            .get_category_summary()
        )

        self.category_section.set_categories(
            categories
        )

    def _load_cash_flow_data(self):

        cash_flow_data = (
            self.dashboard_service
            .get_cash_flow()
        )

        self.cash_flow_section.set_cash_flow(
            cash_flow_data
        )
        
    def _format_variation(
        self,
        variation,
        transaction_type: str,
    ):

        if variation is None:

            return (
                "Sem comparação",
                "#64748B",
            )

        if variation == 0:

            return (
                "0,0%",
                "#94A3B8",
            )

        variation_text = (
            f"{variation:+.1f}%"
            .replace(
                ".",
                ",",
            )
        )

        if transaction_type == "income":

            variation_color = (
                "#34D399"
                if variation > 0
                else "#F87171"
            )

        elif transaction_type == "expense":

            variation_color = (
                "#F87171"
                if variation > 0
                else "#34D399"
            )

        else:

            variation_color = (
                "#34D399"
                if variation > 0
                else "#F87171"
            )

        return (
            variation_text,
            variation_color,
        ) 

    def _format_balance_variation(
        self,
        current_balance,
        previous_balance,
    ):

        variation = (
            current_balance
            - previous_balance
        )

        if variation == 0:

            return (
                "Sem alteração",
                "#94A3B8",
            )

        variation_text = (
            f"{variation:+,.2f}"
            .replace(
                ",",
                "X",
            )
            .replace(
                ".",
                ",",
            )
            .replace(
                "X",
                ".",
            )
        )

        variation_text = (
            f"R$ {variation_text}"
        )

        variation_color = (
            "#34D399"
            if variation > 0
            else "#F87171"
        )

        return (
            variation_text,
            variation_color,
        )

    def refresh(
        self,
    ):

        self._load_summary_data()

        self._load_category_data()

        self._load_cash_flow_data() 