def get_report_style(theme):
    return f"""

QScrollArea#reportScrollArea {{

    background-color: {theme["background"]};

    border: none;

}}


QScrollArea#reportScrollArea QWidget#qt_scrollarea_viewport {{

    background-color: {theme["background"]};

    border: none;

}}


QScrollArea#reportScrollArea QScrollBar:vertical {{

    background-color: transparent;

    width: 8px;

    margin: 4px 2px 4px 2px;

}}


QScrollArea#reportScrollArea QScrollBar::handle:vertical {{

    background-color: {theme["border"]};

    border-radius: 4px;

    min-height: 40px;

}}


QScrollArea#reportScrollArea QScrollBar::handle:vertical:hover {{

    background-color: {theme["secondary_text"]};

}}


QScrollArea#reportScrollArea QScrollBar::add-line:vertical,
QScrollArea#reportScrollArea QScrollBar::sub-line:vertical {{

    background: none;

    border: none;

    height: 0px;

}}


QScrollArea#reportScrollArea QScrollBar::add-page:vertical,
QScrollArea#reportScrollArea QScrollBar::sub-page:vertical {{

    background: transparent;

}}


QWidget#pageContent {{

    background-color: {theme["background"]};

}}


QWidget#reportSection {{

    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-radius: 14px;

}}


QLabel#reportSectionTitle {{

    color: {theme["text"]};

    font-size: 18px;

    font-weight: 600;

    background-color: transparent;

    border: none;

    margin-bottom: 1px;

}}


QLabel#reportSectionSubtitle {{

    color: {theme["secondary_text"]};

    font-size: 13px;

    background-color: transparent;

    border: none;

}}


QLabel#reportChartPlaceholder {{

    color: {theme["secondary_text"]};

    font-size: 13px;

    background-color: transparent;

    border: none;

}}


QWidget#categoryDistributionItem {{

    background-color: transparent;

}}


QLabel#categoryDistributionName {{

    color: {theme["secondary_text"]};

    font-size: 13px;

}}


QLabel#categoryDistributionPercentage {{

    color: {theme["text"]};

    font-size: 13px;

    font-weight: bold;

}}


QFrame#categoryDistributionProgressBackground {{

    background-color: {theme["progress_background"]};

    border-radius: 2px;

}}


QFrame#categoryDistributionProgressBar {{

    border-radius: 2px;

}}

"""