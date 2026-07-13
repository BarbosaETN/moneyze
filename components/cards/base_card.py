from PySide6.QtWidgets import QFrame, QVBoxLayout

class BaseCard(QFrame):
    def __init(self):
        super().__init__()
        self.setObjectName("baseCard")
        self._setup_ui()

    def _setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)