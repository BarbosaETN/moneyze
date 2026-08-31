from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
)

from components.cards.dashboard_summary_card import (
    DashboardSummaryCard,
)


class DashboardSummary(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "dashboardSummary"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QHBoxLayout(
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

    def set_summary(
        self,
        summary_data,
    ):

        self._clear()

        for summary in summary_data:

            card = DashboardSummaryCard(
                title=summary["title"],
                amount=summary["amount"],
                icon_name=summary["icon_name"],
                icon_color=summary["icon_color"],
                icon_background=(
                    summary["icon_background"]
                ),
                variation_text=(
                    summary["variation_text"]
                ),
                variation_color=(
                    summary["variation_color"]
                ),
            )

            self.layout.addWidget(
                card,
                1,
            )

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()