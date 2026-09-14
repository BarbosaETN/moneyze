from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from core.config import DATABASE_PATH
from services.backup_service import BackupService

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
        self.backup_service = BackupService(DATABASE_PATH)

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

        card_layout.addSpacing(
            24
        )

        backup_title = QLabel(
            "Backup e restauração"
        )

        backup_title.setObjectName(
            "backupTitle"
        )

        backup_description = QLabel(
            "Proteja seus dados criando uma cópia do banco."
        )

        backup_description.setObjectName(
            "backupDescription"
        )

        backup_button = QPushButton(
            "Fazer backup"
        )

        backup_button.setObjectName(
            "backupButton"
        )

        backup_button.clicked.connect(
            self._create_backup
        )

        restore_description = QLabel(
            "Restaure seus dados a partir de um backup existente."
        )

        restore_description.setObjectName(
            "backupDescription"
        )

        restore_button = QPushButton(
            "Restaurar backup"
        )

        restore_button.setObjectName(
            "restoreButton"
        )

        restore_button.clicked.connect(
            self._restore_backup
        )

        card_layout.addWidget(
            backup_title
        )

        card_layout.addWidget(
            backup_description
        )

        card_layout.addSpacing(
            10
        )

        card_layout.addWidget(
            backup_button,
            alignment=Qt.AlignmentFlag.AlignLeft,
        )

        card_layout.addSpacing(
            14
        )

        card_layout.addWidget(
            restore_description
        )

        card_layout.addSpacing(
            10
        )

        card_layout.addWidget(
            restore_button,
            alignment=Qt.AlignmentFlag.AlignLeft,
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

    def _create_backup(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Escolher local para salvar o backup",
        )

        if not directory:
            return

        try:
            backup_path = self.backup_service.create_backup(
                directory
            )

            QMessageBox.information(
                self,
                "Backup realizado",
                (
                    "Backup criado com sucesso!\n\n"
                    f"Arquivo: {backup_path.name}"
                ),
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Erro ao criar backup",
                (
                    "Não foi possível criar o backup.\n\n"
                    f"Erro: {error}"
                ),
            )

    def _restore_backup(self):
        backup_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar backup",
            "",
            "Banco SQLite (*.db)",
        )

        if not backup_path:
            return

        if not self.backup_service.validate_backup(
            backup_path
        ):
            QMessageBox.warning(
                self,
                "Backup inválido",
                "O arquivo selecionado não é um backup válido do MoneyZe.",
            )
            return

        confirmation = QMessageBox.question(
            self,
            "Confirmar restauração",
            (
                "A restauração substituirá os dados atuais "
                "do MoneyZe.\n\n"
                "Essa ação não pode ser desfeita. "
                "Deseja continuar?"
            ),
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if confirmation != QMessageBox.StandardButton.Yes:
            return

        try:
            self.backup_service.restore_backup(
                backup_path
            )

            QMessageBox.information(
                self,
                "Restauração concluída",
                (
                    "O backup foi restaurado com sucesso.\n\n"
                    "O MoneyZe será recarregado."
                ),
            )

            window = self.window()

            if hasattr(window, "reload_pages"):
                window.reload_pages()

        except Exception as error:
            QMessageBox.critical(
                self,
                "Erro na restauração",
                (
                    "Não foi possível restaurar o backup.\n\n"
                    f"Erro: {error}"
                ),
            )                