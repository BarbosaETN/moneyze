from styles.colors import (
    PRIMARY,
    PRIMARY_HOVER,
    PRIMARY_PRESSED,
)


BUTTON_STYLE = f"""

QPushButton#primaryButton {{

    background-color: {PRIMARY};

    color: white;

    border: none;

    border-radius: 8px;

    padding: 10px 18px;

    font-weight: bold;

}}

QPushButton#primaryButton:hover {{

    background-color: {PRIMARY_HOVER};

}}

QPushButton#primaryButton:pressed {{

    background-color: {PRIMARY_PRESSED};

}}

"""