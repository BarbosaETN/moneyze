from PySide6.QtWidgets import (
    QHBoxLayout,
    QSizePolicy,
    QWidget,
)


class DashboardContent(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "dashboardContent"
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
            20
        )

    def add_cash_flow_section(
        self,
        widget,
    ):

        widget.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.layout.addWidget(
            widget,
            2,
        )

    def add_category_section(
        self,
        widget,
    ):

        widget.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.layout.addWidget(
            widget,
            1,
        )