from PySide6.QtCore import (
    QObject,
    Signal,
)


class DataEvents(QObject):

    transactions_changed = Signal()


data_events = DataEvents()