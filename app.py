import sys

from PySide6.QtWidgets import QApplication

from database.database import initialize_database
from styles.theme import apply_theme
from views.main_window import MainWindow


def main():
    initialize_database()

    app = QApplication(sys.argv)

    apply_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()