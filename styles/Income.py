from styles.colors import (
    SUCCESS,
)


def get_income_style(theme):
    return f"""

QScrollArea#incomeGrid {{

    background-color: transparent;

    border-radius: 16px;

}}


QScrollArea#incomeGrid QWidget#qt_scrollarea_viewport {{

    background-color: {theme["background"]};

}}


QWidget#incomeGridContainer {{

    background-color: {theme["background"]};

}}


QWidget#incomeHeader {{

    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-bottom: none;

    border-top-left-radius: 16px;

    border-top-right-radius: 16px;

}}


QLabel#incomeHeaderLabel {{

    color: {theme["secondary_text"]};

    font-size: 11px;

    font-weight: bold;

    letter-spacing: 1px;

}}


QWidget#incomeCard {{

    background-color: {theme["background"]};

    border: none;

    border-bottom: 1px solid {theme["border"]};

    border-radius: 0;

}}


QWidget#incomeCard:hover {{

    background-color: {theme["card"]};

}}


QLabel#incomeTitle {{

    color: {theme["text"]};

    font-size: 14px;

    font-weight: bold;

}}


QLabel#incomeDate {{

    color: {theme["secondary_text"]};

    font-size: 12px;

}}


QLabel#incomeCategory {{

    color: {theme["secondary_text"]};

    font-size: 13px;

}}


QLabel#incomeAmount {{

    color: {SUCCESS};

    font-size: 13px;

    font-weight: bold;

}}


QLabel#incomeIcon {{

    background-color: #123D35;

    border-radius: 10px;

}}


QPushButton#incomeDeleteButton {{

    background-color: transparent;

    border: none;

    border-radius: 8px;

}}


QPushButton#incomeDeleteButton:hover {{

    background-color: {theme["border"]};

}}


QPushButton#incomeDeleteButton:pressed {{

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