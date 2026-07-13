from PySide6.QtWidgets import QFrame, QVBoxLayout

class BaseCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("baseCard")

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)