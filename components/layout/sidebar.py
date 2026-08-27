from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from components.layout.navigation import NAVIGATION

from core.config import SIDEBAR_WIDTH


class Sidebar(QWidget):

    page_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")

        self.setFixedWidth(
            SIDEBAR_WIDTH
        )

        self.navigation_buttons = {}

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            16,
            16,
            16,
            16,
        )

        self.layout.setSpacing(8)

        self._create_logo()

        self._create_divider()

        self._create_navigation()

        self.layout.addStretch()

        self._create_user_card()

    def _create_logo(self):

        logo_container = QWidget()

        logo_layout = QHBoxLayout(
            logo_container
        )

        logo_layout.setContentsMargins(
            0,
            0,
            0,
            8,
        )

        logo_layout.setSpacing(10)

        logo_icon = QLabel("M")

        logo_icon.setObjectName(
            "logoIcon"
        )

        logo_icon.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        logo_title = QLabel(
            "MoneyZe"
        )

        logo_title.setObjectName(
            "logoTitle"
        )

        logo_layout.addWidget(
            logo_icon
        )

        logo_layout.addWidget(
            logo_title
        )

        logo_layout.addStretch()

        self.layout.addWidget(
            logo_container
        )

    def _create_divider(self):

        divider = QFrame()

        divider.setObjectName(
            "sidebarDivider"
        )

        divider.setFrameShape(
            QFrame.Shape.HLine
        )

        self.layout.addWidget(
            divider
        )

    def _create_navigation(self):

        self.navigation_container = QWidget()

        navigation_layout = QVBoxLayout(
            self.navigation_container
        )

        navigation_layout.setContentsMargins(
            0,
            12,
            0,
            0,
        )

        navigation_layout.setSpacing(6)

        for item in NAVIGATION:

            button = QPushButton(
                item.title
            )

            button.setObjectName(
                "navigationButton"
            )

            button.setCheckable(True)

            button.setCursor(
                Qt.CursorShape.PointingHandCursor
            )

            button.clicked.connect(
                lambda checked,
                page=item.id:
                self._change_page(page)
            )

            self.navigation_buttons[
                item.id
            ] = button

            navigation_layout.addWidget(
                button
            )

        self.layout.addWidget(
            self.navigation_container
        )

    def _create_user_card(self):

        self.user_card = QWidget()

        self.user_card.setObjectName(
            "userCard"
        )

        user_layout = QVBoxLayout(
            self.user_card
        )

        user_layout.setContentsMargins(
            14,
            14,
            14,
            14,
        )

        user_layout.setSpacing(4)

        user_name = QLabel(
            "Estevan"
        )

        user_name.setObjectName(
            "userName"
        )

        user_status = QLabel(
            "Usuário"
        )

        user_status.setObjectName(
            "userStatus"
        )

        user_layout.addWidget(
            user_name
        )

        user_layout.addWidget(
            user_status
        )

        self.layout.addWidget(
            self.user_card
        )

    def _change_page(
        self,
        page_id: str,
    ):

        self.set_active_page(
            page_id
        )

        self.page_changed.emit(
            page_id
        )

    def set_active_page(
        self,
        page_id: str,
    ):

        for (
            button_id,
            button,
        ) in self.navigation_buttons.items():

            button.setChecked(
                button_id == page_id
            )