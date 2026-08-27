from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
)

import qtawesome as qta

from components.cards.base_card import BaseCard

from styles.category_icons import (
    CATEGORY_ICONS,
    DEFAULT_CATEGORY_ICON,
)

from styles.colors import (
    SUCCESS,
    WARNING,
    DANGER,
    PROGRESS_BACKGROUND,
)


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

        # Define o status visual do orçamento.
        self.setProperty(
            "budgetStatus",
            self._get_budget_status(),
        )

        self._setup_ui()

    def _setup_ui(self):

        self._create_header()

        self._create_spacer()

        self._create_expense_section()

        self._create_progress()

        self._create_footer()

    def _create_header(self):

        header_layout = QHBoxLayout()

        header_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.category_icon = (
            self._create_category_icon()
        )

        title_layout = QVBoxLayout()

        title_layout.setSpacing(4)

        title = QLabel(
            self.name
        )

        title.setObjectName(
            "categoryTitle"
        )

        budget_label = QLabel(
            f"Orçamento: "
            f"{self._format_currency(self.budget)}"
        )

        budget_label.setObjectName(
            "categoryBudget"
        )

        title_layout.addWidget(
            title
        )

        title_layout.addWidget(
            budget_label
        )

        self.delete_button = QPushButton()

        self.delete_button.setObjectName(
            "categoryDeleteButton"
        )

        self.delete_button.setIcon(
            qta.icon(
                "fa5s.trash",
                color="#94A3B8",
            )
        )

        self.delete_button.setFixedSize(
            36,
            36,
        )

        self.delete_button.clicked.connect(
            self._request_delete
        )

        header_layout.addWidget(
            self.category_icon
        )

        header_layout.addSpacing(
            12
        )

        header_layout.addLayout(
            title_layout
        )

        header_layout.addStretch()

        header_layout.addWidget(
            self.delete_button
        )

        self.layout.addLayout(
            header_layout
        )

    def _create_spacer(self):

        spacer = QFrame()

        spacer.setFixedHeight(
            12
        )

        self.layout.addWidget(
            spacer
        )

    def _create_category_icon(self):

        icon_data = CATEGORY_ICONS.get(
            self.name,
            DEFAULT_CATEGORY_ICON,
        )

        icon_container = QLabel()

        icon_container.setObjectName(
            "categoryIcon"
        )

        icon_container.setFixedSize(
            42,
            42,
        )

        icon_container.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        icon = qta.icon(
            icon_data["icon"],
            color=icon_data["color"],
        )

        pixmap = icon.pixmap(
            20,
            20,
        )

        icon_container.setPixmap(
            pixmap
        )

        # Guarda a cor de fundo como propriedade.
        icon_container.setProperty(
            "iconBackground",
            icon_data["background"],
        )

        # Aplica o background específico do ícone.
        icon_container.setStyleSheet(
            f"""
            background-color: {icon_data["background"]};
            border-radius: 21px;
            """
        )

        return icon_container

    def _create_expense_section(self):

        expense_layout = QHBoxLayout()

        expense_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        expense_label = QLabel(
            "Gasto"
        )

        expense_label.setObjectName(
            "categorySectionTitle"
        )

        expense_value = QLabel(
            self._format_currency(
                self.spent
            )
        )

        expense_value.setObjectName(
            "categoryExpenseValue"
        )

        expense_layout.addWidget(
            expense_label
        )

        expense_layout.addStretch()

        expense_layout.addWidget(
            expense_value
        )

        self.layout.addLayout(
            expense_layout
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

        display_percentage = min(
            int(self.percentage),
            100,
        )

        progress.setValue(
            display_percentage
        )

        progress.setTextVisible(
            False
        )

        progress_color = (
            self._get_progress_color()
        )

        progress.setStyleSheet(
            f"""
            QProgressBar {{
                background-color: {PROGRESS_BACKGROUND};
                border: none;
                border-radius: 4px;
                height: 8px;
            }}

            QProgressBar::chunk {{
                background-color: {progress_color};
                border-radius: 4px;
            }}
            """
        )

        self.layout.addWidget(
            progress
        )

    def _create_footer(self):

        footer_layout = QHBoxLayout()

        footer_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        percentage_label = QLabel(
            f"{self.percentage:.0f}% utilizado"
        )

        percentage_label.setObjectName(
            "categoryPercentage"
        )

        percentage_label.setProperty(
            "budgetStatus",
            self._get_budget_status(),
        )

        if self.remaining < 0:

            remaining_label = QLabel(
                f"Excedido: "
                f"{self._format_currency(abs(self.remaining))}"
            )

            remaining_label.setObjectName(
                "categoryExceeded"
            )

        else:

            remaining_label = QLabel(
                f"Restante: "
                f"{self._format_currency(self.remaining)}"
            )

            remaining_label.setObjectName(
                "categoryRemaining"
            )

        footer_layout.addWidget(
            percentage_label
        )

        footer_layout.addStretch()

        footer_layout.addWidget(
            remaining_label
        )

        self.layout.addLayout(
            footer_layout
        )

    def _get_budget_status(self):

        if self.percentage >= 100:
            return "danger"

        if self.percentage >= 80:
            return "warning"

        return "success"

    def _get_progress_color(self):

        if self.percentage >= 100:
            return DANGER

        if self.percentage >= 80:
            return WARNING

        return SUCCESS

    def _format_currency(
        self,
        value: float,
    ):

        return (
            f"R$ {value:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

    def _request_delete(self):

        self.delete_requested.emit(
            self.category_id
        )