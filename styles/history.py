from styles.colors import (
    SUCCESS,
    DANGER,
)


def get_history_style(theme):
    return f"""

QScrollArea#historyGrid {{

    background-color: transparent;

    border: none;

}}


QScrollArea#historyGrid QWidget#qt_scrollarea_viewport {{

    background-color: {theme["background"]};

}}


QWidget#historyGridContainer {{

    background-color: {theme["background"]};

}}


QWidget#historyCard {{

    background-color: {theme["background"]};

    border: none;

    border-bottom: 1px solid {theme["border"]};

    border-radius: 0;

}}


QWidget#historyCard:hover {{

    background-color: {theme["card"]};

}}


QLabel#historyDate {{

    color: {theme["secondary_text"]};

    font-size: 13px;

}}


QLabel#historyHeader {{

    color: {theme["secondary_text"]};

    font-size: 12px;

    font-weight: 500;

    background-color: transparent;

    border: none;

}}


QLabel#historyTitle {{

    color: {theme["text"]};

    font-size: 14px;

    font-weight: bold;

}}


QLabel#historyCategory {{

    color: {theme["secondary_text"]};

    font-size: 13px;

}}


QLabel#historyIncomeAmount {{

    color: {SUCCESS};

    font-size: 13px;

    font-weight: bold;

}}


QLabel#historyExpenseAmount {{

    color: {DANGER};

    font-size: 13px;

    font-weight: bold;

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