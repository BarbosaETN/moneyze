from components.containers.dashboard_summary import (
    DashboardSummary,
)

from components.containers.dashboard_content import (
    DashboardContent,
)

from components.containers.cash_flow_section import (
    CashFlowSection,
)

from components.containers.category_section import (
    CategorySection,
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

        self._setup_page()

    def _setup_page(self):

        self._create_summary()

        self._create_dashboard_content()

    def _create_summary(self):

        self.dashboard_summary = (
            DashboardSummary()
        )

        self.content_layout.addWidget(
            self.dashboard_summary
        )

        self._load_summary_data()

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

        summary_data = [
            {
                "title": "Saldo Total",
                "amount": 24680.00,
                "icon_name": "fa5s.wallet",
                "icon_color": "#34D399",
                "icon_background": "#163B35",
                "variation_text": "↗ +12,4%",
                "variation_color": "#34D399",
            },
            {
                "title": "Receitas",
                "amount": 8500.00,
                "icon_name": "fa5s.arrow-up",
                "icon_color": "#34D399",
                "icon_background": "#163B35",
                "variation_text": "↗ +8,2%",
                "variation_color": "#34D399",
            },
            {
                "title": "Despesas",
                "amount": 5630.00,
                "icon_name": "fa5s.arrow-down",
                "icon_color": "#F87171",
                "icon_background": "#3B2028",
                "variation_text": "↘ +4,1%",
                "variation_color": "#F87171",
            },
            {
                "title": "Economizado",
                "amount": 18550.00,
                "icon_name": "fa5s.piggy-bank",
                "icon_color": "#60A5FA",
                "icon_background": "#1E2D4A",
                "variation_text": "Meta: 74%",
                "variation_color": "#60A5FA",
            },
        ]

        self.dashboard_summary.set_summary(
            summary_data
        )