from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
)

from components.charts.category_distribution_chart import (
    CategoryDistributionChart,
)

from components.containers.category_distribution_list import (
    CategoryDistributionList,
)


class CategoryDistributionSection(QWidget):

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

        self._create_chart_area()

    def _create_header(self):

        title = QLabel(
            "Distribuição por Categoria"
        )

        title.setObjectName(
            "reportSectionTitle"
        )

        subtitle = QLabel(
            "Despesas distribuídas entre categorias"
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

        self.chart_area = QWidget()

        chart_layout = QHBoxLayout(
            self.chart_area
        )

        chart_layout.setContentsMargins(
            0,
            16,
            0,
            0,
        )

        chart_layout.setSpacing(
            32
        )

        self.chart = (
            CategoryDistributionChart()
        )

        self.chart.setMinimumHeight(
            240
        )

        self.category_list = (
            CategoryDistributionList()
        )

        self.category_list.setMinimumHeight(
            240
        )

        chart_layout.addWidget(
            self.chart,
            2,
        )

        chart_layout.addWidget(
            self.category_list,
            3,
        )

        self.layout.addWidget(
            self.chart_area
        )

    def set_category_data(
        self,
        category_data,
    ):

        self.chart.set_data(
            category_data
        )

        self.category_list.set_data(
            category_data
        )