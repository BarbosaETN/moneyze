from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QProgressBar,
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

        self._create_budget_label()

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
            self._get_percentage_text()
        )

        percentage_label.setObjectName(
            self._get_percentage_object_name()
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
            self._get_progress_object_name()
        )

        self.progress_bar.setRange(
            0,
            100,
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

    def _create_budget_label(self):

        budget_label = QLabel(
            self._format_budget_text()
        )

        budget_label.setObjectName(
            self._get_budget_object_name()
        )

        self.layout.addWidget(
            budget_label
        )

    def _get_status(self):

        if self.percentage > 100:

            return "exceeded"

        if self.percentage >= 80:

            return "warning"

        return "normal"

    def _get_percentage_text(self):

        percentage_text = (
            f"{self.percentage:.0f}%"
        )

        status = self._get_status()

        if status == "warning":

            return (
                f"{percentage_text} • Atenção"
            )

        if status == "exceeded":

            return (
                f"{percentage_text} • Ultrapassado"
            )

        return percentage_text

    def _get_percentage_object_name(self):

        status = self._get_status()

        if status == "warning":

            return (
                "dashboardCategoryPercentageWarning"
            )

        if status == "exceeded":

            return (
                "dashboardCategoryPercentageExceeded"
            )

        return (
            "dashboardCategoryPercentage"
        )

    def _get_progress_object_name(self):

        status = self._get_status()

        if status == "warning":

            return (
                "dashboardCategoryProgressWarning"
            )

        if status == "exceeded":

            return (
                "dashboardCategoryProgressExceeded"
            )

        return (
            "dashboardCategoryProgress"
        )

    def _get_budget_object_name(self):

        status = self._get_status()

        if status == "exceeded":

            return (
                "dashboardCategoryBudgetExceeded"
            )

        return (
            "dashboardCategoryBudget"
        )

    def _format_budget_text(self):

        spent = self._format_currency(
            self.spent
        )

        budget = self._format_currency(
            self.budget
        )

        text = (
            f"{spent} de {budget}"
        )

        if self._get_status() == "exceeded":

            return (
                f"{text} • Orçamento ultrapassado"
            )

        return text

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