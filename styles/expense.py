EXPENSE_STYLE = """

QScrollArea#expenseGrid {

    background-color: transparent;

    border-radius: 16px;
}


QScrollArea#expenseGrid QWidget#qt_scrollarea_viewport {

    background-color: #111827;
}


QWidget#expenseGridContainer {

    background-color: #111827;
}


QWidget#expenseCard {

    background-color: #111827;

    border: none;

    border-bottom: 1px solid #263548;

    border-radius: 0;
}


QWidget#expenseCard:hover {

    background-color: #182230;
}


QLabel#expenseTitle {

    color: #E5E7EB;

    font-size: 14px;

    font-weight: bold;
}


QLabel#expenseDate {

    color: #64748B;

    font-size: 12px;
}


QLabel#expenseCategory {

    color: #94A3B8;

    font-size: 13px;
}


QLabel#expenseAmount {

    color: #F87171;

    font-size: 13px;

    font-weight: bold;
}


QLabel#expenseIcon {

    background-color: #3D2028;

    border-radius: 10px;
}


QPushButton#expenseDeleteButton {

    background-color: transparent;

    border: none;

    border-radius: 8px;
}


QPushButton#expenseDeleteButton:hover {

    background-color: #263548;
}


QPushButton#expenseDeleteButton:pressed {

    background-color: #334155;
}


QScrollBar:vertical {

    background-color: transparent;

    width: 8px;

    margin: 4px;
}


QScrollBar::handle:vertical {

    background-color: #334155;

    border-radius: 4px;

    min-height: 30px;
}


QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {

    height: 0px;
}

"""