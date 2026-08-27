from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class Header(QWidget):

    def __init__(
        self,
        title: str,
        subtitle: str = "",
    ):
        super().__init__()

        self.setObjectName("pageHeader")

        self.title = title
        self.subtitle = subtitle

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(4)

        title_label = QLabel(self.title)

        title_label.setObjectName(
            "headerTitle"
        )

        layout.addWidget(
            title_label
        )

        if self.subtitle:

            subtitle_label = QLabel(
                self.subtitle
            )

            subtitle_label.setObjectName(
                "headerSubtitle"
            )

            layout.addWidget(
                subtitle_label
            )