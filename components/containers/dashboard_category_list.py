from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from components.cards.dashboard_category_card import (
    DashboardCategoryCard,
)


class DashboardCategoryList(QScrollArea):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "dashboardCategoryList"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.setWidgetResizable(
            True
        )

        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.content_widget = QWidget()

        self.content_widget.setObjectName(
            "dashboardCategoryListContent"
        )

        self.layout = QVBoxLayout(
            self.content_widget
        )

        self.layout.setContentsMargins(
            0,
            0,
            8,
            0,
        )

        self.layout.setSpacing(
            12
        )

        self.layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        self.setWidget(
            self.content_widget
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