from PySide6.QtWidgets import (
    QLabel,
)

from components.cards.base_card import (
    BaseCard,
)

from components.containers.dashboard_category_list import (
    DashboardCategoryList,
)

from components.empty_states.category_empty_state import (
    CategoryEmptyState,
)


class CategorySection(BaseCard):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "categorySection"
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

        self._create_empty_state()

        self._create_category_list()

        self.show_empty_state()

    def _create_header(self):

        title_label = QLabel(
            "Por Categoria"
        )

        title_label.setObjectName(
            "dashboardSectionTitle"
        )

        subtitle_label = QLabel(
            "Acompanhe seus gastos por categoria"
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

    def _create_empty_state(self):

        self.empty_state = (
            CategoryEmptyState()
        )

        self.layout.addWidget(
            self.empty_state,
            1,
        )

    def _create_category_list(self):

        self.category_list = (
            DashboardCategoryList()
        )

        self.layout.addWidget(
            self.category_list,
            1,
        )

        self.category_list.hide()

    def set_categories(
        self,
        categories,
    ):

        if not categories:

            self.show_empty_state()

            return

        self.show_categories()

        self.category_list.set_categories(
            categories
        )

    def show_empty_state(self):

        self.empty_state.show()

        self.category_list.hide()

    def show_categories(self):

        self.empty_state.hide()

        self.category_list.show()