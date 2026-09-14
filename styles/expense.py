from styles.colors import DANGER


def get_expense_style(theme):
    return f"""

QScrollArea#expenseGrid {{

    background-color: transparent;

    border-radius: 16px;

}}


QScrollArea#expenseGrid QWidget#qt_scrollarea_viewport {{

    background-color: {theme["background"]};

}}


QWidget#expenseGridContainer {{

    background-color: {theme["background"]};

}}


QWidget#expenseCard {{

    background-color: {theme["background"]};

    border: none;

    border-bottom: 1px solid {theme["border"]};

    border-radius: 0;

}}


QWidget#expenseCard:hover {{

    background-color: {theme["card"]};

}}


QLabel#expenseTitle {{

    color: {theme["text"]};

    font-size: 14px;

    font-weight: bold;

}}


QLabel#expenseDate {{

    color: {theme["secondary_text"]};

    font-size: 12px;

}}


QLabel#expenseCategory {{

    color: {theme["secondary_text"]};

    font-size: 13px;

}}


QLabel#expenseAmount {{

    color: {DANGER};

    font-size: 13px;

    font-weight: bold;

}}


QLabel#expenseIcon {{

    background-color: #3D2028;

    border-radius: 10px;

}}


QPushButton#expenseDeleteButton {{

    background-color: transparent;

    border: none;

    border-radius: 8px;

}}


QPushButton#expenseDeleteButton:hover {{

    background-color: {theme["border"]};

}}


QPushButton#expenseDeleteButton:pressed {{

    background-color: {theme["secondary_text"]};

}}


QScrollBar:vertical {{

    background-color: transparent;

    width: 8px;

    margin: 4px;

}}


QScrollBar::handle:vertical {{

    background-color: {theme["border"]};

    border-radius: 4px;

    min-height: 30px;

}}


QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{

    height: 0px;

}}

"""