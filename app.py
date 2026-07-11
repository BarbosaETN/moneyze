import sys

from PySide6.QtWidgets import QApplication

from database.database import initialize_database
from views.main_window import MainWindow

initialize_database()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())