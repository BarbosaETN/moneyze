from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from components.cards.category_distribution_item import (
    CategoryDistributionItem,
)

from core.report_colors import (
    CATEGORY_COLORS,
)


class CategoryDistributionList(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "categoryDistributionList"
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
            16
        )

    def set_data(
        self,
        category_data,
    ):

        self._clear()

        total = sum(
            category["amount"]
            for category in category_data
        )

        for index, category in enumerate(
            category_data
        ):

            percentage = (
                (
                    category["amount"]
                    / total
                )
                * 100
                if total > 0
                else 0
            )

            color = CATEGORY_COLORS[
                index % len(
                    CATEGORY_COLORS
                )
            ]

            item = (
                CategoryDistributionItem(
                    category=category[
                        "category"
                    ],
                    percentage=percentage,
                    color=color,
                )
            )

            self.layout.addWidget(
                item
            )

        self.layout.addStretch()

    def _clear(self):    

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()