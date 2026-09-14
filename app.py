import sys

from PySide6.QtWidgets import QApplication

from database.database import initialize_database
from database.connection import get_session

from repositories.settings_repository import SettingsRepository
from services.settings_service import SettingsService

from styles.theme import apply_theme, DARK_THEME, LIGHT_THEME

from views.main_window import MainWindow


def main():
    initialize_database()

    app = QApplication(sys.argv)

    session = get_session()

    repository = SettingsRepository(session)
    service = SettingsService(repository)

    saved_theme = service.get_setting("theme", "dark")

    print("Tema salvo:", saved_theme)

    if saved_theme == "light":
        theme = LIGHT_THEME
        print("APLICANDO TEMA: CLARO")
    else:
        theme = DARK_THEME
        print("APLICANDO TEMA: ESCURO")

    apply_theme(app, theme)

    session.close()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()