from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from components.charts.monthly_comparison_chart import (
    MonthlyComparisonChart,
)


class MonthlyComparisonSection(QWidget):

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
            20,
            24,
            20,
        )

        self.layout.setSpacing(
            6
        )

        self._create_header()

        self._create_chart()

    def _create_header(self):

        title = QLabel(
            "Comparativo Mensal"
        )

        title.setObjectName(
            "reportSectionTitle"
        )

        subtitle = QLabel(
            "Receitas e despesas ao longo dos meses"
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

    def _create_chart(self):

        self.chart = (
            MonthlyComparisonChart()
        )

        self.chart.setMinimumHeight(
            280
        )

        self.layout.addWidget(
            self.chart,
            1,
        )

    def set_monthly_data(
        self,
        monthly_data,
    ):

        self.chart.set_data(
            monthly_data
        )