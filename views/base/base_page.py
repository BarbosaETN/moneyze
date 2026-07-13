from PySide6.QtWidgets import QVBoxLayout, QWidget
from components.layout.header import Header


class BasePage(QWidget):

    def __init__(self, title: str, subtitle: str = ""):
        super().__init__()

        self._setup_ui(title, subtitle)

    def _setup_ui(self, title: str, subtitle: str):

        self.main_layout = QVBoxLayout(self)

        self.header = Header(title, subtitle)

        self.main_layout.addWidget(self.header)

        self.content = QWidget()

        self.content_layout = QVBoxLayout(self.content)

        self.main_layout.addWidget(self.content)