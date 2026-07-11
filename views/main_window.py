from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from styles.theme import STYLE
from views.sidebar import Sidebar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MoneyZe")
        self.resize(1200, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        self.sidebar = Sidebar()

        content = QWidget()
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        titulo = QLabel("MoneyZe 💰")
        titulo.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        subtitulo = QLabel("Bem-vindo")
        subtitulo.setStyleSheet("""
            font-size: 18px;
            color: gray;
        """)

        content_layout.addWidget(titulo)
        content_layout.addWidget(subtitulo)
        content_layout.addStretch()

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(content, 1)
        
        self.setStyleSheet(STYLE)
        



