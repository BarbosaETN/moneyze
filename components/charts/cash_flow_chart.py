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


class CashFlowChart(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName(
            "cashFlowChart"
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
        cash_flow_data,
    ):

        self._clear()

        chart = (
            self._create_chart(
                cash_flow_data
            )
        )

        chart_view = QChartView(
            chart
        )

        chart_view.setObjectName(
            "cashFlowChartView"
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
        cash_flow_data,
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

        # =========================
        # APARÊNCIA DO CHART
        # =========================

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

        chart.setMargins(
            (
                chart.margins()
            )
        )

        # =========================
        # LEGENDA
        # =========================

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

        # =========================
        # RECEITAS
        # =========================

        income_set = QBarSet(
            "Receitas"
        )

        income_set.setColor(
            QColor(
                "#34D399"
            )
        )

        # =========================
        # DESPESAS
        # =========================

        expense_set = QBarSet(
            "Despesas"
        )

        expense_set.setColor(
            QColor(
                "#F87171"
            )
        )

        # =========================
        # VALORES
        # =========================

        for month in cash_flow_data:

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

        # =========================
        # SÉRIE DE BARRAS
        # =========================

        series = QBarSeries()

        series.setBarWidth(
            0.55
        )

        series.append(
            income_set
        )

        series.append(
            expense_set
        )

        chart.addSeries(
            series
        )

        # =========================
        # EIXO X
        # =========================

        categories = [
            month["label"]
            for month in cash_flow_data
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

        chart.addAxis(
            axis_x,
            Qt.AlignmentFlag.AlignBottom,
        )

        series.attachAxis(
            axis_x
        )

        # =========================
        # EIXO Y
        # =========================

        max_value = (
            self._get_max_value(
                cash_flow_data
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

        chart.addAxis(
            axis_y,
            Qt.AlignmentFlag.AlignLeft,
        )

        series.attachAxis(
            axis_y
        )

        return chart

    def _get_max_value(
        self,
        cash_flow_data,
    ):

        values = []

        for month in cash_flow_data:

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