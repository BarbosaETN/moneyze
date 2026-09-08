from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QFrame,
    QLineEdit,
)

from database.connection import get_session
from repositories.settings_repository import SettingsRepository
from services.settings_service import SettingsService
from views.base.base_page import BasePage
from styles.theme import apply_theme


class SettingsPage(BasePage):
    def __init__(self):
        super().__init__(
            "Configurações",
            "Personalize as preferências do MoneyZe.",
        )

        self.session = get_session()
        self.repository = SettingsRepository(self.session)
        self.service = SettingsService(self.repository)

        self._loading_settings = True

        self._build_ui()
        self._load_settings()

    def _build_ui(self):
        preferences_card = QFrame()
        preferences_card.setObjectName("settingsCard")

        layout = QFormLayout(preferences_card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setHorizontalSpacing(30)
        layout.setVerticalSpacing(18)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Digite seu nome")

        self.theme_combo = QComboBox()
        self.theme_combo.addItems([
            "Sistema",
            "Claro",
            "Escuro",
        ])

        self.currency_combo = QComboBox()
        self.currency_combo.addItem("BRL - Real brasileiro", "BRL")
        self.currency_combo.addItem("USD - Dólar americano", "USD")
        self.currency_combo.addItem("EUR - Euro", "EUR")

        layout.addRow("Seu nome", self.name_input)
        layout.addRow("Tema", self.theme_combo)
        layout.addRow("Moeda", self.currency_combo)

        self.content_layout.addWidget(preferences_card)
        self.content_layout.addStretch()

        self.name_input.editingFinished.connect(self._save_name)
        self.currency_combo.currentIndexChanged.connect(self._save_currency)
        self.theme_combo.currentIndexChanged.connect(self._save_theme)

    def _load_settings(self):
        name = self.service.get_setting("user_name", "")
        currency = self.service.get_setting("currency", "BRL")
        theme = self.service.get_setting("theme", "dark")

        self.name_input.setText(name)

        currency_index = self.currency_combo.findData(currency)

        if currency_index >= 0:
            self.currency_combo.setCurrentIndex(currency_index)

        theme_map = {
            "system": "Sistema",
            "light": "Claro",
            "dark": "Escuro",
        }

        theme_index = self.theme_combo.findText(
            theme_map.get(theme, "Escuro")
        )

        if theme_index >= 0:
            self.theme_combo.setCurrentIndex(theme_index)

    def _save_name(self):
        name = self.name_input.text().strip()

        self.service.set_setting("user_name", name)

    def _save_currency(self):
        currency = self.currency_combo.currentData()

        self.service.set_setting("currency", currency)

    def _save_theme(self):
        if self._loading_settings:
            return

        theme = self.theme_combo.currentText()

        if theme == "Claro":
            theme_value = "light"
        elif theme == "Escuro":
            theme_value = "dark"
        else:
            theme_value = "system"

        self.service.set_setting("theme", theme_value)

        app = QApplication.instance()

        if app:
            if theme_value == "light":
                apply_theme(app, "light")
            else:
                apply_theme(app, "dark")        