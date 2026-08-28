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

"""


def apply_theme(app):

    app.setStyleSheet(
        THEME
    )