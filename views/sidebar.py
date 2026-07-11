from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout()

        botoes = [
            "Dashboard",
            "Receitas",
            "Despesas",
            "Histórico",
            "Categorias",
            "Relatórios",
            "Configurações",
        ]

        for texto in botoes:
            botao = QPushButton(texto)
            botao.setMaximumHeight(45)
            layout.addWidget(botao)

        layout.addStretch()

        self.setLayout(layout)