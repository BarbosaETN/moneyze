from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton

from components.buttons.primary_button import PrimaryButton
from components.dialogs.base_dialog import BaseDialog

class CategoryDialog(BaseDialog):
    def __init__(self):
        super().__init__("Nova Categoria")

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        self._create_form()

        self._create_buttons()

    def _create_form(self):

        self.name_label = QLabel("Nome")
        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Digite o nome da categoria"
        )

        self.main_layout.addWidget(self.name_label)
        self.main_layout.addWidget(self.name_input)

    def _create_buttons(self):

        buttons_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Cancelar")

        self.save_button = PrimaryButton("Salvar")

        buttons_layout.addWidget(self.cancel_button)

        buttons_layout.addWidget(self.save_button)

        self.main_layout.addLayout(buttons_layout)

    def _connect_signals(self):

        self.cancel_button.clicked.connect(self.reject)

        self.save_button.clicked.connect(self.accept)

    def get_data(self):

        return {
            "name": self.name_input.text().strip()
        }

