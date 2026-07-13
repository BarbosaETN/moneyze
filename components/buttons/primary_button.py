from PySide6.QtWidgets import QPushButton

class PrimaryButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)

        self.setObjectName("primaryButton")