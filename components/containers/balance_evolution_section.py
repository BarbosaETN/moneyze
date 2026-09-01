from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
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

        self.chart_placeholder = QLabel(
            "Gráfico de evolução do saldo"
        )

        self.chart_placeholder.setObjectName(
            "reportChartPlaceholder"
        )

        self.chart_placeholder.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.chart_placeholder.setMinimumHeight(
            220
        )

        self.layout.addWidget(
            self.chart_placeholder
        )