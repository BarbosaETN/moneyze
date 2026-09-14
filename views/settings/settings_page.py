from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)

from database.connection import get_session
from repositories.settings_repository import SettingsRepository
from services.settings_service import SettingsService
from views.base.base_page import BasePage

from styles.theme import (
    DARK_THEME,
    LIGHT_THEME,
    apply_theme,
)


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

        self._loading_settings = False

    def _build_ui(self):
        preferences_card = QFrame()
        preferences_card.setObjectName(
            "settingsCard"
        )

        preferences_card.setMaximumWidth(
            760
        )

        card_layout = QVBoxLayout(
            preferences_card
        )

        card_layout.setContentsMargins(
            24,
            24,
            24,
            24,
        )

        card_layout.setSpacing(
            6
        )

        title = QLabel(
            "Preferências gerais"
        )

        title.setObjectName(
            "settingsTitle"
        )

        description = QLabel(
            "Configure as principais preferências do aplicativo."
        )

        description.setObjectName(
            "settingsDescription"
        )

        card_layout.addWidget(
            title
        )

        card_layout.addWidget(
            description
        )

        card_layout.addSpacing(
            18
        )

        form_layout = QFormLayout()

        form_layout.setHorizontalSpacing(
            30
        )

        form_layout.setVerticalSpacing(
            18
        )

        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Digite seu nome"
        )

        self.theme_combo = QComboBox()

        self.theme_combo.addItems([
            "Sistema",
            "Claro",
            "Escuro",
        ])

        self.currency_combo = QComboBox()

        self.currency_combo.addItem(
            "BRL - Real brasileiro",
            "BRL",
        )

        self.currency_combo.addItem(
            "USD - Dólar americano",
            "USD",
        )

        self.currency_combo.addItem(
            "EUR - Euro",
            "EUR",
        )

        form_layout.addRow(
            "Seu nome",
            self.name_input,
        )

        form_layout.addRow(
            "Tema",
            self.theme_combo,
        )

        form_layout.addRow(
            "Moeda",
            self.currency_combo,
        )

        card_layout.addLayout(
            form_layout
        )

        self.content_layout.addWidget(
            preferences_card
        )

        self.content_layout.addStretch()

        self.name_input.editingFinished.connect(
            self._save_name
        )

        self.currency_combo.currentIndexChanged.connect(
            self._save_currency
        )

        self.theme_combo.currentIndexChanged.connect(
            self._save_theme
        )

    def _load_settings(self):
        name = self.service.get_setting(
            "user_name",
            "",
        )

        currency = self.service.get_setting(
            "currency",
            "BRL",
        )

        theme = self.service.get_setting(
            "theme",
            "dark",
        )

        self.name_input.setText(
            name
        )

        currency_index = self.currency_combo.findData(
            currency
        )

        if currency_index >= 0:
            self.currency_combo.setCurrentIndex(
                currency_index
            )

        theme_map = {
            "system": "Sistema",
            "light": "Claro",
            "dark": "Escuro",
        }

        theme_index = self.theme_combo.findText(
            theme_map.get(
                theme,
                "Escuro",
            )
        )

        if theme_index >= 0:
            self.theme_combo.setCurrentIndex(
                theme_index
            )

    def _save_name(self):
        name = self.name_input.text().strip()

        self.service.set_setting(
            "user_name",
            name,
        )

    def _save_currency(self):
        currency = self.currency_combo.currentData()

        self.service.set_setting(
            "currency",
            currency,
        )

    def _save_theme(self):
        if self._loading_settings:
            return

        theme = self.theme_combo.currentText()

        if theme == "Claro":
            theme_value = "light"
            selected_theme = LIGHT_THEME

        elif theme == "Escuro":
            theme_value = "dark"
            selected_theme = DARK_THEME

        else:
            theme_value = "system"
            selected_theme = DARK_THEME

        self.service.set_setting(
            "theme",
            theme_value,
        )

        app = QApplication.instance()

        if app:
            apply_theme(
                app,
                selected_theme,
            )