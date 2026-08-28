from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)


class MonthSelector(QWidget):

    previous_requested = Signal()
    next_requested = Signal()

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "monthSelector"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(
            12
        )

        self.previous_button = QPushButton(
            "‹"
        )

        self.previous_button.setObjectName(
            "monthNavigationButton"
        )

        self.previous_button.setFixedSize(
            36,
            36,
        )

        self.month_label = QLabel()

        self.month_label.setObjectName(
            "monthLabel"
        )

        self.month_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.month_label.setFixedWidth(
            150
        )

        self.next_button = QPushButton(
            "›"
        )

        self.next_button.setObjectName(
            "monthNavigationButton"
        )

        self.next_button.setFixedSize(
            36,
            36,
        )

        self.previous_button.clicked.connect(
            self.previous_requested.emit
        )

        self.next_button.clicked.connect(
            self.next_requested.emit
        )

        layout.addStretch()

        layout.addWidget(
            self.previous_button
        )

        layout.addWidget(
            self.month_label
        )

        layout.addWidget(
            self.next_button
        )

        layout.addStretch()

    def set_month_text(
        self,
        text: str,
    ):

        self.month_label.setText(
            text
        )