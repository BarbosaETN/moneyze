from styles.button import BUTTON_STYLE

from styles.card import CARD_STYLE

from styles.header import HEADER_STYLE

from styles.sidebar import SIDEBAR_STYLE

from styles.category_card import CATEGORY_CARD_STYLE

from styles.month_selector import (
    MONTH_SELECTOR_STYLE,
)

from styles.income import INCOME_STYLE

from styles.expense import EXPENSE_STYLE

from styles.transaction import TRANSACTION_STYLE

from styles.summary_card import SUMMARY_CARD_STYLE

from styles.empty_state import EMPTY_STATE_STYLE

from styles.history  import HISTORY_STYLE

from styles.history_filters import HISTORY_FILTERS_STYLE

from styles.dashboard_summary import DASHBOARD_SUMMARY_STYLE

from styles.dashboard_summary import CASH_FLOW_SECTION_STYLE

from styles.dashboard_summary import DASHBOARD_CATEGORY_LIST_STYLE

from styles.dashboard_summary import DASHBOARD_CATEGORY_CARD_STYLE

from styles.dashboard_summary import CATEGORY_SECTION_STYLE

from styles.dashboard_summary import CASH_FLOW_EMPTY_STATE_STYLE

from styles.dashboard_summary import CATEGORY_EMPTY_STATE_STYLE


THEME = f"""

{BUTTON_STYLE}

{CARD_STYLE}

{HEADER_STYLE}

{SIDEBAR_STYLE}

{CATEGORY_CARD_STYLE}

{MONTH_SELECTOR_STYLE}

{INCOME_STYLE}

{EXPENSE_STYLE}

{TRANSACTION_STYLE}

{SUMMARY_CARD_STYLE}

{EMPTY_STATE_STYLE}

{HISTORY_STYLE}

{HISTORY_FILTERS_STYLE}

{DASHBOARD_SUMMARY_STYLE}

{CASH_FLOW_SECTION_STYLE}

{DASHBOARD_CATEGORY_LIST_STYLE}

{DASHBOARD_CATEGORY_CARD_STYLE}

{CATEGORY_SECTION_STYLE}

{CASH_FLOW_EMPTY_STATE_STYLE}

{CATEGORY_EMPTY_STATE_STYLE}

"""


def apply_theme(app):

    app.setStyleSheet(
        THEME
    )