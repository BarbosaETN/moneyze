from styles.colors import (
    SUCCESS,
    WARNING,
    DANGER,
)


def get_dashboard_summary_style(theme):
    return f"""

QWidget#dashboardSummaryCard {{
    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-radius: 14px;
}}


QLabel#dashboardSummaryTitle {{
    color: {theme["secondary_text"]};

    font-size: 13px;

    font-weight: 500;
}}


QLabel#dashboardSummaryAmount {{
    color: {theme["text"]};

    font-size: 24px;

    font-weight: 700;
}}


QLabel#dashboardSummaryVariation {{
    font-size: 12px;

    font-weight: 600;
}}

"""


def get_cash_flow_section_style(theme):
    return f"""

QFrame#cashFlowSection {{
    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-radius: 14px;
}}


QLabel#dashboardSectionTitle {{
    color: {theme["text"]};

    font-size: 16px;

    font-weight: 600;

    border: none;

    background: transparent;
}}


QLabel#dashboardSectionSubtitle {{
    color: {theme["secondary_text"]};

    font-size: 12px;

    border: none;

    background: transparent;
}}


QLabel#cashFlowPlaceholder {{
    color: {theme["secondary_text"]};

    font-size: 13px;

    border: none;

    background: transparent;
}}

"""


def get_dashboard_category_list_style(theme):
    return f"""

QScrollArea#dashboardCategoryList {{
    background-color: transparent;

    border: none;
}}


QWidget#dashboardCategoryListContent {{
    background-color: transparent;
}}


QScrollArea#dashboardCategoryList QScrollBar:vertical {{
    background-color: transparent;

    width: 8px;

    margin: 4px 0px 4px 0px;

    border: none;
}}


QScrollArea#dashboardCategoryList QScrollBar::handle:vertical {{
    background-color: {theme["border"]};

    border-radius: 4px;

    min-height: 30px;
}}


QScrollArea#dashboardCategoryList QScrollBar::handle:vertical:hover {{
    background-color: {theme["secondary_text"]};
}}


QScrollArea#dashboardCategoryList QScrollBar::add-line:vertical,
QScrollArea#dashboardCategoryList QScrollBar::sub-line:vertical {{
    height: 0px;

    background-color: transparent;

    border: none;
}}


QScrollArea#dashboardCategoryList QScrollBar::add-page:vertical,
QScrollArea#dashboardCategoryList QScrollBar::sub-page:vertical {{
    background-color: transparent;
}}

"""


def get_dashboard_category_card_style(theme):
    return f"""

QFrame#dashboardCategoryCard {{
    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-radius: 12px;
}}


QLabel#dashboardCategoryName {{
    color: {theme["text"]};

    font-size: 13px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}}


QLabel#dashboardCategoryPercentage {{
    color: {theme["secondary_text"]};

    font-size: 12px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}}


QLabel#dashboardCategoryPercentageWarning {{
    color: {WARNING};

    font-size: 12px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}}


QLabel#dashboardCategoryPercentageExceeded {{
    color: {DANGER};

    font-size: 12px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}}


QLabel#dashboardCategoryBudget {{
    color: {theme["secondary_text"]};

    font-size: 11px;

    background-color: transparent;

    border: none;
}}


QLabel#dashboardCategoryBudgetExceeded {{
    color: {DANGER};

    font-size: 11px;

    font-weight: 500;

    background-color: transparent;

    border: none;
}}


QProgressBar#dashboardCategoryProgress {{
    background-color: {theme["progress_background"]};

    border: none;

    border-radius: 4px;

    height: 8px;
}}


QProgressBar#dashboardCategoryProgress::chunk {{
    background-color: {SUCCESS};

    border-radius: 4px;
}}


QProgressBar#dashboardCategoryProgressWarning {{
    background-color: {theme["progress_background"]};

    border: none;

    border-radius: 4px;

    height: 8px;
}}


QProgressBar#dashboardCategoryProgressWarning::chunk {{
    background-color: {WARNING};

    border-radius: 4px;
}}


QProgressBar#dashboardCategoryProgressExceeded {{
    background-color: {theme["progress_background"]};

    border: none;

    border-radius: 4px;

    height: 8px;
}}


QProgressBar#dashboardCategoryProgressExceeded::chunk {{
    background-color: {DANGER};

    border-radius: 4px;
}}

"""


def get_category_section_style(theme):
    return f"""

QFrame#categorySection {{
    background-color: transparent;

    border: none;
}}


QLabel#categoryEmptyState {{
    color: {theme["secondary_text"]};

    font-size: 13px;

    background-color: transparent;

    border: none;
}}

"""


def get_cash_flow_empty_state_style(theme):
    return f"""

QWidget#cashFlowEmptyState {{
    background-color: transparent;

    border: none;
}}


QLabel#cashFlowEmptyStateTitle {{
    color: {theme["text"]};

    font-size: 14px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}}


QLabel#cashFlowEmptyStateDescription {{
    color: {theme["secondary_text"]};

    font-size: 12px;

    background-color: transparent;

    border: none;
}}

"""


def get_category_empty_state_style(theme):
    return f"""

QWidget#categoryEmptyState {{
    background-color: transparent;

    border: none;
}}


QLabel#categoryEmptyStateTitle {{
    color: {theme["text"]};

    font-size: 14px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}}


QLabel#categoryEmptyStateDescription {{
    color: {theme["secondary_text"]};

    font-size: 12px;

    background-color: transparent;

    border: none;
}}

"""