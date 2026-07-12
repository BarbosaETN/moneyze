from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from components.layout.sidebar import Sidebar
from core.config import APP_NAME, WINDOW_HEIGHT, WINDOW_WIDTH

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self._setup_ui()


    def _setup_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout()
        central_widget.setLayout(self.main_layout)
        self.sidebar = Sidebar()
        self.content_widget = QWidget()
        self.content_layout = QHBoxLayout()
        self.content_widget.setLayout(self.content_layout)
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content_widget)

        



