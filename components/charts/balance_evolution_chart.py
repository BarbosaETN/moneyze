from PySide6.QtCharts import (
    QChart,
    QChartView,
    QCategoryAxis,
    QLineSeries,
    QValueAxis,
)

from PySide6.QtCore import (
    Qt,
    QMargins,
)

from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
)

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)


class BalanceEvolutionChart(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "balanceEvolutionChart"
        )

        self._setup_ui()

    def _setup_ui(self):

        self.layout = QVBoxLayout(
            self
        )

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.layout.setSpacing(
            0
        )

    def set_data(
        self,
        balance_data,
    ):

        self._clear()

        chart = (
            self._create_chart(
                balance_data
            )
        )

        chart_view = QChartView(
            chart
        )

        chart_view.setObjectName(
            "balanceEvolutionChartView"
        )

        chart_view.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        chart_view.setBackgroundBrush(
            QColor(
                "#182230"
            )
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
        balance_data,
    ):

        chart = QChart()

        chart.setMargins(
            QMargins(
                10,
                10,
                10,
                10,
            )
        )

        self._configure_chart(
            chart
        )

        series = (
            self._create_series(
                balance_data
            )
        )

        chart.addSeries(
            series
        )

        axis_x = (
            self._create_x_axis(
                balance_data
            )
        )

        axis_y = (
            self._create_y_axis(
                balance_data
            )
        )

        chart.addAxis(
            axis_x,
            Qt.AlignmentFlag.AlignBottom,
        )

        chart.addAxis(
            axis_y,
            Qt.AlignmentFlag.AlignLeft,
        )

        series.attachAxis(
            axis_x
        )

        series.attachAxis(
            axis_y
        )

        return chart

    def _configure_chart(
        self,
        chart,
    ):

        chart.setBackgroundVisible(
            True
        )

        chart.setBackgroundBrush(
            QColor(
                "#182230"
            )
        )

        chart.setPlotAreaBackgroundVisible(
            True
        )

        chart.setPlotAreaBackgroundBrush(
            QColor(
                "#182230"
            )
        )

        chart.legend().setVisible(
            False
        )

    def _create_series(
        self,
        balance_data,
    ):

        series = QLineSeries()

        series.setName(
            "Saldo"
        )

        series.setPen(
            QPen(
                QColor(
                    "#3B82F6"
                ),
                3,
            )
        )

        for index, month in enumerate(
            balance_data
        ):

            series.append(
                index + 0.5,
                float(
                    month["balance"]
                ),
            )

        return series

    def _create_x_axis(
        self,
        balance_data,
    ):

        axis_x = QCategoryAxis()

        for index, month in enumerate(
            balance_data
        ):

            axis_x.append(
                month["label"],
                index + 1,
            )

        axis_x.setRange(
            0,
            len(balance_data),
        )

        axis_x.setLabelsColor(
            QColor(
                "#94A3B8"
            )
        )

        axis_x.setLinePen(
            QPen(
                QColor(
                    "#263548"
                )
            )
        )

        axis_x.setGridLineVisible(
            False
        )

        return axis_x

    def _create_y_axis(
        self,
        balance_data,
    ):

        max_value = (
            self._get_max_value(
                balance_data
            )
        )

        min_value = (
            self._get_min_value(
                balance_data
            )
        )

        axis_y = QValueAxis()

        axis_y.setRange(
            min_value,
            max_value,
        )

        axis_y.setLabelFormat(
            "R$ %.0f"
        )

        axis_y.setTickCount(
            5
        )

        axis_y.setLabelsColor(
            QColor(
                "#94A3B8"
            )
        )

        axis_y.setLinePen(
            QPen(
                QColor(
                    "#263548"
                )
            )
        )

        axis_y.setGridLineColor(
            QColor(
                "#263548"
            )
        )

        return axis_y

    def _get_max_value(
        self,
        balance_data,
    ):

        values = [
            month["balance"]
            for month in balance_data
        ]

        if not values:

            return 100

        max_value = max(
            values
        )

        if max_value == 0:

            return 100

        return max_value * 1.2

    def _get_min_value(
        self,
        balance_data,
    ):

        values = [
            month["balance"]
            for month in balance_data
        ]

        if not values:

            return 0

        min_value = min(
            values
        )

        if min_value >= 0:

            return 0

        return min_value * 1.2

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()