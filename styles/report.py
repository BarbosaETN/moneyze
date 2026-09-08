REPORT_STYLE = """

QScrollArea#reportScrollArea {

    background-color: #0B1220;

    border: none;

}


QScrollArea#reportScrollArea QWidget#qt_scrollarea_viewport {

    background-color: #0B1220;

    border: none;

}


QScrollArea#reportScrollArea QScrollBar:vertical {

    background-color: transparent;

    width: 8px;

    margin: 4px 2px 4px 2px;

}


QScrollArea#reportScrollArea QScrollBar::handle:vertical {

    background-color: #263548;

    border-radius: 4px;

    min-height: 40px;

}


QScrollArea#reportScrollArea QScrollBar::handle:vertical:hover {

    background-color: #334155;

}


QScrollArea#reportScrollArea QScrollBar::add-line:vertical,
QScrollArea#reportScrollArea QScrollBar::sub-line:vertical {

    background: none;

    border: none;

    height: 0px;

}


QScrollArea#reportScrollArea QScrollBar::add-page:vertical,
QScrollArea#reportScrollArea QScrollBar::sub-page:vertical {

    background: transparent;

}


QWidget#pageContent {

    background-color: #0B1220;

}


QWidget#reportSection {

    background-color: #182230;

    border: 1px solid #263548;

    border-radius: 14px;

}


QLabel#reportSectionTitle {

    color: #E5E7EB;

    font-size: 18px;

    font-weight: 600;

    background-color: transparent;

    border: none;

    margin-bottom: 1px;

}


QLabel#reportSectionSubtitle {

    color: #94A3B8;

    font-size: 13px;

    background-color: transparent;

    border: none;

}


QLabel#reportChartPlaceholder {

    color: #64748B;

    font-size: 13px;

    background-color: transparent;

    border: none;

}


QWidget#categoryDistributionItem {

    background-color: transparent;

}


QLabel#categoryDistributionName {

    color: #94A3B8;

    font-size: 13px;

}


QLabel#categoryDistributionPercentage {

    color: #E5E7EB;

    font-size: 13px;

    font-weight: bold;

}


QFrame#categoryDistributionProgressBackground {

    background-color: #263548;

    border-radius: 2px;

}


QFrame#categoryDistributionProgressBar {

    border-radius: 2px;

}

"""