from styles.button import BUTTON_STYLE
from styles.card import get_card_style
from styles.header import get_header_style
from styles.sidebar import get_sidebar_style
from styles.category_card import get_category_card_style
from styles.month_selector import get_month_selector_style
from styles.income import INCOME_STYLE
from styles.expense import EXPENSE_STYLE
from styles.transaction import TRANSACTION_STYLE
from styles.summary_card import SUMMARY_CARD_STYLE
from styles.empty_state import EMPTY_STATE_STYLE
from styles.history import HISTORY_STYLE
from styles.history_filters import HISTORY_FILTERS_STYLE

from styles.dashboard_summary import get_dashboard_summary_style
from styles.dashboard_summary import get_cash_flow_section_style
from styles.dashboard_summary import get_dashboard_category_list_style
from styles.dashboard_summary import get_dashboard_category_card_style
from styles.dashboard_summary import get_category_section_style
from styles.dashboard_summary import get_cash_flow_empty_state_style
from styles.dashboard_summary import get_category_empty_state_style

from styles.report import get_report_style

from styles.themes import DARK_THEME, LIGHT_THEME


def build_theme(theme=None):
    if theme is None:
        theme = DARK_THEME

    return f"""

{BUTTON_STYLE}

{get_card_style(theme)}

{get_header_style(theme)}

{get_sidebar_style(theme)}

{get_category_card_style(theme)}

{get_month_selector_style(theme)}

{INCOME_STYLE}

{EXPENSE_STYLE}

{TRANSACTION_STYLE}

{SUMMARY_CARD_STYLE}

{EMPTY_STATE_STYLE}

{HISTORY_STYLE}

{HISTORY_FILTERS_STYLE}

{get_dashboard_summary_style(theme)}

{get_cash_flow_section_style(theme)}

{get_dashboard_category_list_style(theme)}

{get_dashboard_category_card_style(theme)}

{get_category_section_style(theme)}

{get_cash_flow_empty_state_style(theme)}

{get_category_empty_state_style(theme)}

{get_report_style(theme)}

"""


def apply_theme(app, theme=None):
    app.setStyleSheet(build_theme(LIGHT_THEME))