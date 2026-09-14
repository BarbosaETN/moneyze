def get_summary_card_style(theme):
    return f"""

QWidget#summaryCard {{

    background-color: {theme["card"]};

    border: 1px solid {theme["border"]};

    border-radius: 16px;

}}


QLabel#summaryTitle {{

    color: {theme["secondary_text"]};

    font-size: 13px;

    font-weight: 500;

}}


QLabel#summaryAmount {{

    color: #34D399;

    font-size: 26px;

    font-weight: bold;

}}

"""