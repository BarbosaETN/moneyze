from styles.colors import (
    PRIMARY,
    PRIMARY_HOVER,
)

BUTTON_STYLE = f"""
QPushButton {{

    background-color: {PRIMARY};

    color: white;

    border: none;

    border-radius: 8px;

    padding: 8px 16px;
}}

QPushButton:hover {{

    background-color: {PRIMARY_HOVER};

}}
"""