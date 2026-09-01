from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QValueAxis,
)

from PySide6.QtCore import (
    Qt,
    QMargins,
)

from PySide6.QtGui import (
    QColor,
    QFont,
    QPainter,
    QPen,
)

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)


class MonthlyComparisonChart(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "monthlyComparisonChart"
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
        comparison_data,
    ):

        self._clear()

        chart = (
            self._create_chart(
                comparison_data
            )
        )

        chart_view = QChartView(
            chart
        )

        chart_view.setObjectName(
            "monthlyComparisonChartView"
        )

        chart_view.setMinimumHeight(
            280
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
        comparison_data,
    ):

        chart = QChart()

        chart.setMargins(
            QMargins(
                12,
                12,
                12,
                12,
            )
        )

        self._configure_chart(
            chart
        )

        series = (
            self._create_series(
                comparison_data
            )
        )

        chart.addSeries(
            series
        )

        axis_x = (
            self._create_x_axis(
                comparison_data
            )
        )

        axis_y = (
            self._create_y_axis(
                comparison_data
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
            True
        )

        chart.legend().setAlignment(
            Qt.AlignmentFlag.AlignBottom
        )

        chart.legend().setLabelColor(
            QColor(
                "#94A3B8"
            )
        )

        legend_font = QFont()

        legend_font.setPointSize(
            10
        )

        chart.legend().setFont(
            legend_font
        )

    def _create_series(
        self,
        comparison_data,
    ):

        income_set = QBarSet(
            "Receitas"
        )

        income_set.setColor(
            QColor(
                "#34D399"
            )
        )

        expense_set = QBarSet(
            "Despesas"
        )

        expense_set.setColor(
            QColor(
                "#F87171"
            )
        )

        for month in comparison_data:

            income_set.append(
                float(
                    month["income"]
                )
            )

            expense_set.append(
                float(
                    month["expense"]
                )
            )

        series = QBarSeries()

        series.setBarWidth(
            0.48
        )

        series.append(
            income_set
        )

        series.append(
            expense_set
        )

        return series

    def _create_x_axis(
        self,
        comparison_data,
    ):

        categories = [
            month["label"]
            for month in comparison_data
        ]

        axis_x = QBarCategoryAxis()

        axis_x.append(
            categories
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
        comparison_data,
    ):

        max_value = (
            self._get_max_value(
                comparison_data
            )
        )

        axis_y = QValueAxis()

        axis_y.setRange(
            0,
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
        comparison_data,
    ):

        values = []

        for month in comparison_data:

            values.append(
                month["income"]
            )

            values.append(
                month["expense"]
            )

        if not values:

            return 100

        max_value = max(
            values
        )

        if max_value == 0:

            return 100

        return (
            max_value
            * 1.2
        )

    def _clear(self):

        while self.layout.count():

            item = self.layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()