from PySide6.QtCharts import (
    QChart,
    QChartView,
    QPieSeries,
)

from PySide6.QtCore import (
    Qt,
)

from PySide6.QtGui import (
    QColor,
    QPainter,
)

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)


class CategoryDistributionChart(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "categoryDistributionChart"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QVBoxLayout(
            self
        )

        self.layout.setContentsMargins(
            0,
            16,
            0,
            0,
        )

        self.layout.setSpacing(
            0
        )

    def set_data(
        self,
        category_data,
    ):

        self._clear()

        chart = (
            self._create_chart(
                category_data
            )
        )

        chart_view = QChartView(
            chart
        )

        chart_view.setObjectName(
            "categoryDistributionChartView"
        )

        chart_view.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        chart_view.setStyleSheet(
            """
            background-color: #182230;
            border: none;
            """
        )

        self.layout.addWidget(
            chart_view
        )

    def _create_chart(
        self,
        category_data,
    ):

        chart = QChart()

        chart.setBackgroundVisible(
            True
        )

        chart.setBackgroundBrush(
            QColor(
                "#182230"
            )
        )

        chart.setPlotAreaBackgroundVisible(
            False
        )

        chart.legend().setVisible(
            False
        )

        series = (
            self._create_series(
                category_data
            )
        )

        chart.addSeries(
            series
        )

        return chart

    def _create_series(
        self,
        category_data,
    ):

        series = QPieSeries()

        series.setHoleSize(
            0.55
        )

        series.setPieSize(
            0.75
        )

        colors = [
            "#3B82F6",
            "#34D399",
            "#F59E0B",
            "#F87171",
            "#A78BFA",
            "#22D3EE",
            "#FB7185",
            "#A3E635",
        ]

        for index, category in enumerate(
            category_data
        ):

            slice_ = series.append(
                category["category"],
                float(
                    category["amount"]
                ),
            )

            color = colors[
                index % len(colors)
            ]

            slice_.setColor(
                QColor(
                    color
                )
            )

            slice_.setLabelVisible(
                False
            )

        return series

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()