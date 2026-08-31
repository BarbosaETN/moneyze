from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
)

from components.cards.base_card import (
    BaseCard,
)

from components.containers.dashboard_category_list import (
    DashboardCategoryList,
)


class CategorySection(BaseCard):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "categorySection"
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
            16
        )

        self._create_title()
        self._create_category_list()

    def _create_title(self):

        title_label = QLabel(
            "Por Categoria"
        )

        title_label.setObjectName(
            "dashboardSectionTitle"
        )

        self.layout.addWidget(
            title_label
        )

    def _create_category_list(self):

        self.category_list = (
            DashboardCategoryList()
        )

        self.layout.addWidget(
            self.category_list,
            1,
        )