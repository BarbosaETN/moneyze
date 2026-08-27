from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class EmptyState(QWidget):

    def __init__(
        self,
        title: str,
        description: str,
    ):
        super().__init__()

        self.title = title
        self.description = description

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(8)

        self.title_label = QLabel(
            self.title
        )

        self.title_label.setObjectName(
            "emptyStateTitle"
        )

        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.description_label = QLabel(
            self.description
        )

        self.description_label.setObjectName(
            "emptyStateDescription"
        )

        self.description_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.description_label.setWordWrap(True)

        layout.addWidget(
            self.title_label
        )

        layout.addWidget(
            self.description_label
        )

    def set_content(
        self,
        title: str,
        description: str,
    ):

        self.title_label.setText(
            title
        )

        self.description_label.setText(
            description
        )    