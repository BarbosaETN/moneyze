from styles.colors import PRIMARY


def get_history_filters_style(theme):
    return f"""

QWidget#historyFilters {{

    background-color: transparent;

}}


QLineEdit#historySearchInput {{

    background-color: {theme["card"]};

    color: {theme["text"]};

    border: 1px solid {theme["border"]};

    border-radius: 10px;

    padding: 10px 14px;

    font-size: 10pt;

}}


QLineEdit#historySearchInput:focus {{

    border: 1px solid {PRIMARY};

}}


QComboBox#historyTypeFilter,
QComboBox#historyPeriodFilter {{

    background-color: {theme["card"]};

    color: {theme["text"]};

    border: 1px solid {theme["border"]};

    border-radius: 10px;

    padding: 8px 14px;

    min-width: 120px;

    font-size: 10pt;

}}


QComboBox#historyTypeFilter:hover,
QComboBox#historyPeriodFilter:hover {{

    border: 1px solid {theme["secondary_text"]};

}}


QComboBox#historyTypeFilter::drop-down,
QComboBox#historyPeriodFilter::drop-down {{

    border: none;

    width: 30px;

}}


QComboBox#historyTypeFilter QAbstractItemView,
QComboBox#historyPeriodFilter QAbstractItemView {{

    background-color: {theme["card"]};

    color: {theme["text"]};

    border: 1px solid {theme["border"]};

    selection-background-color: {theme["border"]};

    font-size: 10pt;

}}

"""