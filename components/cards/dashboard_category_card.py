from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)

from components.cards.base_card import (
    BaseCard,
)


class DashboardCategoryCard(BaseCard):

    def __init__(
        self,
        name: str,
        budget: float,
        spent: float,
        percentage: float,
    ):
        super().__init__()

        self.name = name
        self.budget = budget
        self.spent = spent
        self.percentage = percentage

        self.setObjectName(
            "dashboardCategoryCard"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout.setContentsMargins(
            20,
            16,
            20,
            16,
        )

        self.layout.setSpacing(
            10
        )

        self._create_content()

    def _create_content(self):

        self._create_header()
        self._create_progress_bar()

    def _create_header(self):

        header_layout = QHBoxLayout()

        self._create_name_label(
            header_layout
        )

        self._create_percentage_label(
            header_layout
        )

        self.layout.addLayout(
            header_layout
        )

    def _create_name_label(
        self,
        layout,
    ):

        name_label = QLabel(
            self.name
        )

        name_label.setObjectName(
            "dashboardCategoryName"
        )

        name_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            name_label
        )

    def _create_percentage_label(
        self,
        layout,
    ):

        percentage_label = QLabel(
            f"{self.percentage:.0f}%"
        )

        percentage_label.setObjectName(
            "dashboardCategoryPercentage"
        )

        percentage_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(
            percentage_label
        )

    def _create_progress_bar(self):

        self.progress_bar = QProgressBar()

        self.progress_bar.setObjectName(
            "dashboardCategoryProgress"
        )

        self.progress_bar.setRange(
            0,
            100
        )

        progress_value = min(
            int(self.percentage),
            100,
        )

        self.progress_bar.setValue(
            progress_value
        )

        self.progress_bar.setTextVisible(
            False
        )

        self.layout.addWidget(
            self.progress_bar
        )

        self._create_budget_label()

    def _create_budget_label(self):

        budget_label = QLabel(
            self._format_budget_text()
        )

        budget_label.setObjectName(
            "dashboardCategoryBudget"
        )

        self.layout.addWidget(
            budget_label
        )

    def _format_budget_text(self):

        spent = self._format_currency(
            self.spent
        )

        budget = self._format_currency(
            self.budget
        )

        return (
            f"{spent} de {budget}"
        )

    def _format_currency(
        self,
        value: float,
    ):

        formatted_value = (
            f"{value:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return (
            f"R$ {formatted_value}"
        )