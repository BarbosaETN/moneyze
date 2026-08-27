from styles.colors import (
    CARD,
    TEXT,
    SECONDARY_TEXT,
    BORDER,
)


MONTH_SELECTOR_STYLE = f"""

#monthSelector {{

    background-color: transparent;

}}

#monthLabel {{

    color: {TEXT};

    font-size: 16px;

    font-weight: bold;

    padding: 0 8px;

}}

QPushButton#monthNavigationButton {{

    background-color: {CARD};

    color: {SECONDARY_TEXT};

    border: 1px solid {BORDER};

    border-radius: 8px;

    font-size: 18px;

    font-weight: bold;

}}

QPushButton#monthNavigationButton:hover {{

    color: {TEXT};

    border: 1px solid {SECONDARY_TEXT};

}}

QPushButton#monthNavigationButton:pressed {{

    background-color: {BORDER};

}}

"""