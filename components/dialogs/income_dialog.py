from PySide6.QtCore import QDate

from PySide6.QtWidgets import (
    QDateEdit,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)

from components.buttons.primary_button import PrimaryButton
from components.dialogs.base_dialog import BaseDialog


class IncomeDialog(BaseDialog):

    def __init__(self):
        super().__init__(
            "Nova Receita"
        )

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):

        self._create_form()
        self._create_buttons()

    def _create_form(self):

        title_label = QLabel(
            "Título"
        )

        self.title_input = QLineEdit()

        self.title_input.setPlaceholderText(
            "Ex.: Salário"
        )


        amount_label = QLabel(
            "Valor"
        )

        self.amount_input = QDoubleSpinBox()

        self.amount_input.setRange(
            0.01,
            999999999.99,
        )

        self.amount_input.setDecimals(
            2
        )

        self.amount_input.setPrefix(
            "R$ "
        )


        date_label = QLabel(
            "Data"
        )

        self.date_input = QDateEdit()

        self.date_input.setCalendarPopup(
            True
        )

        self.date_input.setDate(
            QDate.currentDate()
        )


        description_label = QLabel(
            "Descrição"
        )

        self.description_input = QTextEdit()

        self.description_input.setPlaceholderText(
            "Descrição opcional"
        )


        self.main_layout.addWidget(
            title_label
        )

        self.main_layout.addWidget(
            self.title_input
        )


        self.main_layout.addWidget(
            amount_label
        )

        self.main_layout.addWidget(
            self.amount_input
        )


        self.main_layout.addWidget(
            date_label
        )

        self.main_layout.addWidget(
            self.date_input
        )


        self.main_layout.addWidget(
            description_label
        )

        self.main_layout.addWidget(
            self.description_input
        )

    def _create_buttons(self):

        layout = QHBoxLayout()

        self.cancel_button = QPushButton(
            "Cancelar"
        )

        self.save_button = PrimaryButton(
            "Salvar"
        )

        layout.addWidget(
            self.cancel_button
        )

        layout.addWidget(
            self.save_button
        )

        self.main_layout.addLayout(
            layout
        )

    def _connect_signals(self):

        self.cancel_button.clicked.connect(
            self.reject
        )

        self.save_button.clicked.connect(
            self.accept
        )

    def get_data(self):

        return {
            "title": (
                self.title_input
                .text()
                .strip()
            ),

            "amount": (
                self.amount_input
                .value()
            ),

            "transaction_date": (
                self.date_input
                .date()
                .toPython()
            ),

            "description": (
                self.description_input
                .toPlainText()
                .strip()
                or None
            ),
        }