HISTORY_FILTERS_STYLE = """

QWidget#historyFilters {
    background-color: transparent;
}

QLineEdit#historySearchInput {
    background-color: #182230;

    color: #E5E7EB;

    border: 1px solid #263548;

    border-radius: 10px;

    padding: 10px 14px;

    font-size: 10pt;
}

QLineEdit#historySearchInput:focus {
    border: 1px solid #34D399;
}

QComboBox#historyTypeFilter,
QComboBox#historyPeriodFilter {
    background-color: #182230;

    color: #E5E7EB;

    border: 1px solid #263548;

    border-radius: 10px;

    padding: 8px 14px;

    min-width: 120px;

    font-size: 10pt;
}

QComboBox#historyTypeFilter:hover,
QComboBox#historyPeriodFilter:hover {
    border: 1px solid #334155;
}

QComboBox#historyTypeFilter::drop-down,
QComboBox#historyPeriodFilter::drop-down {
    border: none;

    width: 30px;
}

QComboBox#historyTypeFilter QAbstractItemView,
QComboBox#historyPeriodFilter QAbstractItemView {
    background-color: #182230;

    color: #E5E7EB;

    border: 1px solid #263548;

    selection-background-color: #263548;

    font-size: 10pt;
}

"""