from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from components.layout.navigation import NAVIGATION
from core.config import SIDEBAR_WIDTH


class Sidebar(QWidget):

    page_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(SIDEBAR_WIDTH)

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QVBoxLayout(self)

        self._create_logo()

        self._create_navigation()

        self.layout.addStretch()

        self._create_user_card()

    def _create_logo(self):

        logo = QLabel("MoneyZe")

        self.layout.addWidget(logo)

    def _create_navigation(self):

        for item in NAVIGATION:

            button = QPushButton(item.title)

            button.clicked.connect(
                lambda _, page=item.id: self.page_changed.emit(page)
            )

            self.layout.addWidget(button)

    def _create_user_card(self):

        user = QLabel("Estevan")

        self.layout.addWidget(user)