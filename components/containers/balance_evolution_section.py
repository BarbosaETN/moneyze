from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from components.charts.balance_evolution_chart import (
    BalanceEvolutionChart,
)


class BalanceEvolutionSection(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "reportSection"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QVBoxLayout(
            self
        )

        self.layout.setContentsMargins(
            24,
            18,
            24,
            18,
        )

        self.layout.setSpacing(
            8
        )

        self._create_header()

        self._create_chart_area()

    def _create_header(self):

        title = QLabel(
            "Evolução do Saldo"
        )

        title.setObjectName(
            "reportSectionTitle"
        )

        subtitle = QLabel(
            "Saldo acumulado ao longo do período"
        )

        subtitle.setObjectName(
            "reportSectionSubtitle"
        )

        self.layout.addWidget(
            title
        )

        self.layout.addWidget(
            subtitle
        )

    def _create_chart_area(self):

        self.chart = (
            BalanceEvolutionChart()
        )

        self.chart.setMinimumHeight(
            240
        )

        self.layout.addWidget(
            self.chart
        )

    def set_balance_data(
        self,
        balance_data,
    ):

        self.chart.set_data(
            balance_data
        )