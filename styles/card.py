def get_card_style(theme):
    return f"""

#baseCard {{

    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-radius: 16px;

}}

"""