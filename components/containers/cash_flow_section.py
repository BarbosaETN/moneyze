from PySide6.QtWidgets import (
    QLabel,
)

from components.cards.base_card import (
    BaseCard,
)

from components.charts.cash_flow_chart import (
    CashFlowChart,
)

from components.empty_states.cash_flow_empty_state import (
    CashFlowEmptyState,
)


class CashFlowSection(BaseCard):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "cashFlowSection"
        )

        self.setMinimumHeight(
            360
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout.setContentsMargins(
            24,
            22,
            24,
            22,
        )

        self.layout.setSpacing(
            6
        )

        self._create_header()

        self._create_content()

    def _create_header(self):

        title_label = QLabel(
            "Fluxo de Caixa"
        )

        title_label.setObjectName(
            "dashboardSectionTitle"
        )

        subtitle_label = QLabel(
            "Acompanhe a evolução das suas finanças"
        )

        subtitle_label.setObjectName(
            "dashboardSectionSubtitle"
        )

        self.layout.addWidget(
            title_label
        )

        self.layout.addWidget(
            subtitle_label
        )

    def _create_content(self):

        self.cash_flow_chart = (
            CashFlowChart()
        )

        self.cash_flow_empty_state = (
            CashFlowEmptyState()
        )

        self.layout.addWidget(
            self.cash_flow_chart,
            1,
        )

        self.layout.addWidget(
            self.cash_flow_empty_state,
            1,
        )

        self.cash_flow_empty_state.hide()

    def set_cash_flow(
        self,
        cash_flow_data,
    ):

        has_transactions = (
            self._has_transactions(
                cash_flow_data
            )
        )

        if has_transactions:

            self.cash_flow_empty_state.hide()

            self.cash_flow_chart.show()

            self.cash_flow_chart.set_data(
                cash_flow_data
            )

        else:

            self.cash_flow_chart.hide()

            self.cash_flow_empty_state.show()

    def _has_transactions(
        self,
        cash_flow_data,
    ):

        return any(
            month["income"] > 0
            or month["expense"] > 0
            for month in cash_flow_data
        )