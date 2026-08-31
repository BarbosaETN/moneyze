from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QLabel,
    QStackedLayout,
    QWidget,
)

from components.cards.base_card import (
    BaseCard,
)

from components.empty_state import (
    EmptyState,
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

        self.content_widget = QWidget()

        self.content_widget.setObjectName(
            "cashFlowContent"
        )

        self.content_layout = QStackedLayout(
            self.content_widget
        )

        self._create_empty_state()
        self._create_chart_placeholder()

        self.layout.addWidget(
            self.content_widget,
            1,
        )

    def _create_empty_state(self):

        self.empty_state = EmptyState(
            title=(
                "Nenhum dado disponível"
            ),
            description=(
                "Adicione receitas e despesas "
                "para acompanhar seu fluxo."
            ),
        )

        self.content_layout.addWidget(
            self.empty_state
        )

    def _create_chart_placeholder(self):

        self.chart_placeholder = QLabel(
            "Gráfico de fluxo de caixa"
        )

        self.chart_placeholder.setObjectName(
            "cashFlowChartPlaceholder"
        )

        self.chart_placeholder.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.content_layout.addWidget(
            self.chart_placeholder
        )

    def show_empty_state(self):

        self.content_layout.setCurrentWidget(
            self.empty_state
        )

    def show_chart(self):

        self.content_layout.setCurrentWidget(
            self.chart_placeholder
        )