from styles.button import get_button_style
from styles.card import get_card_style
from styles.header import get_header_style
from styles.sidebar import get_sidebar_style
from styles.category_card import get_category_card_style
from styles.month_selector import get_month_selector_style
from styles.income import get_income_style
from styles.expense import get_expense_style
from styles.transaction import get_transaction_style
from styles.summary_card import get_summary_card_style
from styles.empty_state import get_empty_state_style
from styles.history import get_history_style
from styles.history_filters import get_history_filters_style

from styles.dashboard_summary import get_dashboard_summary_style
from styles.dashboard_summary import get_cash_flow_section_style
from styles.dashboard_summary import get_dashboard_category_list_style
from styles.dashboard_summary import get_dashboard_category_card_style
from styles.dashboard_summary import get_category_section_style
from styles.dashboard_summary import get_cash_flow_empty_state_style
from styles.dashboard_summary import get_category_empty_state_style

from styles.report import get_report_style
from styles.settings import get_settings_style

from styles.themes import DARK_THEME, LIGHT_THEME


def build_theme(theme=None):
    if theme is None:
        theme = DARK_THEME

    return f"""
{get_button_style(theme)}

{get_card_style(theme)}

{get_header_style(theme)}

{get_sidebar_style(theme)}

{get_category_card_style(theme)}

{get_month_selector_style(theme)}

{get_income_style(theme)}

{get_expense_style(theme)}

{get_transaction_style(theme)}

{get_summary_card_style(theme)}

{get_empty_state_style(theme)}

{get_history_style(theme)}

{get_history_filters_style(theme)}

{get_dashboard_summary_style(theme)}

{get_cash_flow_section_style(theme)}

{get_dashboard_category_list_style(theme)}

{get_dashboard_category_card_style(theme)}

{get_category_section_style(theme)}

{get_cash_flow_empty_state_style(theme)}

{get_category_empty_state_style(theme)}

{get_report_style(theme)}

{get_settings_style(theme)}
"""


def apply_theme(app, theme=None):
    if theme is None:
        theme = DARK_THEME

    app.setStyleSheet(build_theme(theme))