import qtawesome as qta

from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class EmptyState(QWidget):

    action_requested = Signal()

    def __init__(
        self,
        title: str,
        description: str,
        icon_name: str = None,
        icon_color: str = "#64748B",
        button_text: str = None,
        button_icon: str = None,
    ):
        super().__init__()

        self.title = title
        self.description = description
        self.icon_name = icon_name
        self.icon_color = icon_color
        self.button_text = button_text
        self.button_icon = button_icon

        self.setObjectName(
            "emptyState"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout(
            self
        )

        layout.setContentsMargins(
            24,
            24,
            24,
            24,
        )

        layout.setSpacing(
            12
        )

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self._create_icon()

        self._create_title()

        self._create_description()

        self._create_button()

    def _create_icon(self):

        if not self.icon_name:

            self.icon_label = None

            return

        self.icon_label = QLabel()

        self.icon_label.setObjectName(
            "emptyStateIcon"
        )

        self.icon_label.setFixedSize(
            56,
            56,
        )

        self.icon_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        icon = qta.icon(
            self.icon_name,
            color=self.icon_color,
        )

        self.icon_label.setPixmap(
            icon.pixmap(
                28,
                28,
            )
        )

        self.layout().addWidget(
            self.icon_label,
            alignment=(
                Qt.AlignmentFlag.AlignCenter
            ),
        )

    def _create_title(self):

        self.title_label = QLabel(
            self.title
        )

        self.title_label.setObjectName(
            "emptyStateTitle"
        )

        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title_label.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Maximum,
        )

        self.layout().addWidget(
            self.title_label,
            alignment=(
                Qt.AlignmentFlag.AlignCenter
            ),
        )

    def _create_description(self):

        self.description_label = QLabel(
            self.description
        )

        self.description_label.setObjectName(
            "emptyStateDescription"
        )

        self.description_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.description_label.setWordWrap(
            True
        )

        self.description_label.setFixedWidth(
            360
        )

        self.description_label.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Preferred,
        )

        self.layout().addWidget(
            self.description_label,
            alignment=(
                Qt.AlignmentFlag.AlignCenter
            ),
        )

    def _create_button(self):

        if not self.button_text:

            self.action_button = None

            return

        self.action_button = QPushButton(
            self.button_text
        )

        self.action_button.setObjectName(
            "emptyStateButton"
        )

        if self.button_icon:

            icon = qta.icon(
                self.button_icon,
                color="#FFFFFF",
            )

            self.action_button.setIcon(
                icon
            )

        self.action_button.clicked.connect(
            self.action_requested.emit
        )

        self.layout().addWidget(
            self.action_button,
            alignment=(
                Qt.AlignmentFlag.AlignCenter
            ),
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

        self.description_label.adjustSize()