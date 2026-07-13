from styles.button import BUTTON_STYLE

from styles.card import CARD_STYLE

from styles.header import HEADER_STYLE

from styles.sidebar import SIDEBAR_STYLE


THEME = f"""
{BUTTON_STYLE}

{CARD_STYLE}

{HEADER_STYLE}

{SIDEBAR_STYLE}
"""

def apply_theme(app):
    app.setStyleSheet(THEME)