from styles.colors import (
    CARD,
    BORDER,
    TEXT,
    SECONDARY_TEXT,
    PRIMARY,
)


MONTH_SELECTOR_STYLE = f"""

#monthSelector {{
    background-color: transparent;
}}

QPushButton#monthNavigationButton {{
    background-color: {CARD};
    color: {TEXT};

    border: 1px solid {BORDER};
    border-radius: 10px;

    font-size: 24px;
    font-weight: bold;
}}

QPushButton#monthNavigationButton:hover {{
    border-color: {PRIMARY};
    color: {PRIMARY};
}}

QPushButton#monthNavigationButton:pressed {{
    background-color: {BORDER};
}}

#monthLabel {{
    color: {TEXT};

    font-size: 16px;
    font-weight: bold;
}}

"""