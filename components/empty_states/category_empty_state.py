from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class CategoryEmptyState(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "categoryEmptyState"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout(
            self
        )

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(
            8
        )

        self._create_title()

        self._create_description()

    def _create_title(self):

        title_label = QLabel(
            "Nenhuma categoria cadastrada"
        )

        title_label.setObjectName(
            "categoryEmptyStateTitle"
        )

        title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.layout().addWidget(
            title_label
        )

    def _create_description(self):

        description_label = QLabel(
            (
                "Crie categorias para acompanhar "
                "seus gastos mensais."
            )
        )

        description_label.setObjectName(
            "categoryEmptyStateDescription"
        )

        description_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        description_label.setWordWrap(
            True
        )

        self.layout().addWidget(
            description_label
        )