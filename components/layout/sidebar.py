from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from components.layout.navigation import NAVIGATION

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(250)

        self._setup_ui()

    def _setup_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._create_logo()
        self._create_navigation()
        self.layout.addStretch()
        self._create_user_card()

    def _create_logo(self):

        logo = QLabel("MoneyZe")
        self.layout.addWidget(logo)

    def _create_navigation(self):

        for text in NAVIGATION:

            button = QPushButton(text)
            self.layout.addWidget(button)

    def _create_user_card(self):
        user = QLabel("Estevan")
        self.layout.addWidget(user)
        