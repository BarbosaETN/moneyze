from styles.colors import PRIMARY


def get_month_selector_style(theme):
    return f"""

#monthSelector {{
    background-color: transparent;
}}


QPushButton#monthNavigationButton {{
    background-color: {theme["card"]};
    color: {theme["text"]};

    border: 1px solid {theme["border"]};
    border-radius: 10px;

    font-size: 24px;
    font-weight: bold;
}}


QPushButton#monthNavigationButton:hover {{
    border-color: {PRIMARY};
    color: {PRIMARY};
}}


QPushButton#monthNavigationButton:pressed {{
    background-color: {theme["border"]};
}}


#monthLabel {{
    color: {theme["text"]};

    font-size: 16px;
    font-weight: bold;
}}

"""