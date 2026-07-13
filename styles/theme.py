from styles.button import BUTTON_STYLE

from styles.card import CARD_STYLE

from styles.header import HEADER_STYLE

from styles.sidebar import SIDEBAR_STYLE

from styles.category_card import CATEGORY_CARD_STYLE


THEME = f"""
{BUTTON_STYLE}

{CARD_STYLE}

{HEADER_STYLE}

{SIDEBAR_STYLE}

{CATEGORY_CARD_STYLE}
"""

def apply_theme(app):
    app.setStyleSheet(THEME)