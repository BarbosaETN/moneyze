from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QWidget,
)


class HistoryFilters(QWidget):

    filters_changed = Signal()

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "historyFilters"
        )

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):

        self.layout = QHBoxLayout(
            self
        )

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.layout.setSpacing(
            16
        )

        self._create_search_input()
        self._create_type_filter()
        self._create_period_filter()

    def _create_search_input(self):

        self.search_input = QLineEdit()

        self.search_input.setObjectName(
            "historySearchInput"
        )

        self.search_input.setPlaceholderText(
            "Buscar movimentação..."
        )

        self.layout.addWidget(
            self.search_input,
            1,
        )

    def _create_type_filter(self):

        self.type_filter = QComboBox()

        self.type_filter.setObjectName(
            "historyTypeFilter"
        )

        self.type_filter.addItem(
            "Todos"
        )

        self.type_filter.addItem(
            "Receitas"
        )

        self.type_filter.addItem(
            "Despesas"
        )

        self.layout.addWidget(
            self.type_filter
        )

    def _create_period_filter(self):

        self.period_filter = QComboBox()

        self.period_filter.setObjectName(
            "historyPeriodFilter"
        )

        self.period_filter.addItem(
            "Todos"
        )

        self.period_filter.addItem(
            "Este mês"
        )

        self.period_filter.addItem(
            "Mês passado"
        )

        self.layout.addWidget(
            self.period_filter
        )

    def _connect_signals(self):

        self.search_input.textChanged.connect(
            lambda _: self.filters_changed.emit()
        )

        self.type_filter.currentIndexChanged.connect(
            lambda _: self.filters_changed.emit()
        )

        self.period_filter.currentIndexChanged.connect(
            lambda _: self.filters_changed.emit()
        )

    def get_search_text(self):

        return (
            self.search_input.text()
        )

    def get_selected_type(self):

        return (
            self.type_filter.currentText()
        )

    def get_selected_period(self):

        return (
            self.period_filter.currentText()
        )