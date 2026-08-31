from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from components.cards.dashboard_category_card import (
    DashboardCategoryCard,
)


class DashboardCategoryList(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "dashboardCategoryList"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QVBoxLayout(
            self
        )

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.layout.setSpacing(
            12
        )

    def set_categories(
        self,
        categories,
    ):

        self._clear()

        for category in categories:

            self._add_category(
                category
            )

    def _add_category(
        self,
        category,
    ):

        card = DashboardCategoryCard(
            name=category["name"],
            budget=category["budget"],
            spent=category["spent"],
            percentage=category["percentage"],
        )

        self.layout.addWidget(
            card
        )

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()