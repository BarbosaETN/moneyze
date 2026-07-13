from PySide6.QtWidgets import (
    QLabel,
    QProgressBar,
)

from components.cards.base_card import BaseCard


class CategoryCard(BaseCard):

    def __init__(
        self,
        name: str,
        budget: float,
        spent: float,
    ):
        super().__init__()

        self.name = name
        self.budget = budget
        self.spent = spent

        self.remaining = budget - spent

        self.percentage = (
            (self.spent / self.budget) * 100
            if self.budget > 0
            else 0
        )

        self._setup_ui()

    def _setup_ui(self):

        self._create_header()

        self._create_section(
            "Orçamento",
            f"R$ {self.budget:.2f}",
        )

        self._create_section(
            "Gasto",
            f"R$ {self.spent:.2f}",
        )

        self._create_progress()

        self._create_section(
            "Restante",
            f"R$ {self.remaining:.2f}",
        )

    def _create_header(self):

        title = QLabel(self.name)
        title.setObjectName("categoryTitle")

        self.layout.addWidget(title)

    def _create_section(
        self,
        title: str,
        value: str,
    ):

        title_label = QLabel(title)
        title_label.setObjectName("categorySectionTitle")

        value_label = QLabel(value)
        value_label.setObjectName("categorySectionValue")

        self.layout.addWidget(title_label)
        self.layout.addWidget(value_label)

    def _create_progress(self):

        progress = QProgressBar()

        progress.setObjectName("categoryProgress")

        progress.setRange(0, 100)

        progress.setValue(int(self.percentage))

        self.layout.addWidget(progress)