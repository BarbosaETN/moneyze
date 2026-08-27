from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
)

from components.cards.base_card import BaseCard
from utils.formatters import format_currency


class CategoryCard(BaseCard):

    delete_requested = Signal(int)

    def __init__(
        self,
        category_id: int,
        name: str,
        budget: float,
        spent: float,
        remaining: float,
        percentage: float,
    ):
        super().__init__()

        self.category_id = category_id
        self.name = name
        self.budget = budget
        self.spent = spent
        self.remaining = remaining
        self.percentage = percentage

        self._setup_ui()

    def _setup_ui(self):

        self._create_header()

        self._create_section(
            "Orçamento",
            format_currency(self.budget),
        )

        self._create_section(
            "Gasto",
            format_currency(self.spent),
        )

        self._create_budget_warning()

        self._create_progress()

        self._create_percentage_label()

        remaining_object_name = (
            "categoryExceededValue"
            if self._is_budget_exceeded()
            else "categorySectionValue"
        )

        self._create_section(
            "Restante",
            format_currency(self.remaining),
            remaining_object_name,
        )

    def _create_header(self):

        header_layout = QHBoxLayout()

        title = QLabel(self.name)

        title.setObjectName(
            "categoryTitle"
        )

        self.delete_button = QPushButton(
            "🗑"
        )

        self.delete_button.setObjectName(
            "deleteButton"
        )

        self.delete_button.clicked.connect(
            self._request_delete
        )

        header_layout.addWidget(title)

        header_layout.addStretch()

        header_layout.addWidget(
            self.delete_button
        )

        self.layout.addLayout(
            header_layout
        )

    def _create_section(
        self,
        title: str,
        value: str,
        value_object_name="categorySectionValue",
    ):

        title_label = QLabel(title)

        title_label.setObjectName(
            "categorySectionTitle"
        )

        value_label = QLabel(value)

        value_label.setObjectName(
            value_object_name
        )

        self.layout.addWidget(
            title_label
        )

        self.layout.addWidget(
            value_label
        )

    def _create_budget_warning(self):

        if not self._is_budget_exceeded():
            return

        warning_label = QLabel(
            "Orçamento ultrapassado"
        )

        warning_label.setObjectName(
            "categoryBudgetWarning"
        )

        self.layout.addWidget(
            warning_label
        )

    def _create_progress(self):

        progress = QProgressBar()

        progress.setObjectName(
            "categoryProgress"
        )

        progress.setRange(
            0,
            100,
        )

        progress_value = min(
            int(self.percentage),
            100,
        )

        progress.setValue(
            progress_value
        )

        self.layout.addWidget(
            progress
        )

    def _create_percentage_label(self):

        percentage_label = QLabel(
            f"{self.percentage:.1f}% utilizado"
        )

        object_name = (
            "categoryExceededPercentage"
            if self._is_budget_exceeded()
            else "categoryPercentage"
        )

        percentage_label.setObjectName(
            object_name
        )

        self.layout.addWidget(
            percentage_label
        )

    def _is_budget_exceeded(self):

        return (
            self.budget > 0
            and self.spent > self.budget
        )

    def _request_delete(self):

        self.delete_requested.emit(
            self.category_id
        )