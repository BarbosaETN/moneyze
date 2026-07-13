from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QStackedWidget,
)

from components.layout.navigation import NAVIGATION
from components.layout.sidebar import Sidebar
from core.config import (
    APP_NAME,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Armazena as instâncias das páginas
        self.pages = {}

        self._setup_ui()
        self._create_pages()

        self.sidebar.page_changed.connect(self.change_page)

        # Página inicial
        self.change_page("dashboard")

    def _setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QHBoxLayout(central_widget)

        self.sidebar = Sidebar()

        # Área onde as páginas serão exibidas
        self.content = QStackedWidget()

        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content)

    def _create_pages(self):

        for item in NAVIGATION:

            page = item.page()

            self.pages[item.id] = page

            self.content.addWidget(page)

    def change_page(self, page_id: str):

        page = self.pages.get(page_id)

        if page:
            self.content.setCurrentWidget(page)