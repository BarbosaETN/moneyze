from PySide6.QtCore import (
    Qt,
)

from PySide6.QtGui import (
    QColor,
)

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class CategoryDistributionItem(QWidget):

    def __init__(
        self,
        category,
        percentage,
        color,
    ):

        super().__init__()

        self.category = category
        self.percentage = percentage
        self.color = color

        self.setObjectName(
            "categoryDistributionItem"
        )

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout(
            self
        )

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(
            6
        )

        self._create_header(
            layout
        )

        self._create_progress_bar(
            layout
        )

    def _create_header(
        self,
        layout,
    ):

        header_layout = QHBoxLayout()

        header_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        header_layout.setSpacing(
            8
        )

        category_layout = QHBoxLayout()

        category_layout.setSpacing(
            8
        )

        color_indicator = QLabel()

        color_indicator.setFixedSize(
            8,
            8,
        )

        color_indicator.setStyleSheet(
            f"""
            background-color: {self.color};
            border-radius: 4px;
            """
        )

        category_label = QLabel(
            self.category
        )

        category_label.setObjectName(
            "categoryDistributionName"
        )

        category_layout.addWidget(
            color_indicator
        )

        category_layout.addWidget(
            category_label
        )

        percentage_label = QLabel(
            f"{self.percentage:.0f}%"
        )

        percentage_label.setObjectName(
            "categoryDistributionPercentage"
        )

        header_layout.addLayout(
            category_layout
        )

        header_layout.addStretch()

        header_layout.addWidget(
            percentage_label
        )

        layout.addLayout(
            header_layout
        )

    def _create_progress_bar(
        self,
        layout,
    ):

        progress_background = QFrame()

        progress_background.setObjectName(
            "categoryDistributionProgressBackground"
        )

        progress_background.setFixedHeight(
            4
        )

        progress_layout = QHBoxLayout(
            progress_background
        )

        progress_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        progress_layout.setSpacing(
            0
        )

        progress_bar = QFrame()

        progress_bar.setObjectName(
            "categoryDistributionProgressBar"
        )

        progress_bar.setStyleSheet(
            f"""
            background-color: {self.color};
            border-radius: 2px;
            """
        )

        empty_space = QWidget()

        progress_layout.addWidget(
            progress_bar,
            int(
                self.percentage
            )
        )

        progress_layout.addWidget(
            empty_space,
            int(
                100 - self.percentage
            )
        )

        layout.addWidget(
            progress_background
        )