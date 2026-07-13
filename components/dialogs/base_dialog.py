from PySide6.QtWidgets import QDialog, QVBoxLayout

class BaseDialog(QDialog):
    def __init__(self, title: str):
        super().__init__()

        self.setWindowTitle(title)
        self.setModal(True)
        self.resize(420, 250)

        self.main_layout = QVBoxLayout(self)