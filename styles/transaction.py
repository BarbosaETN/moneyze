def get_transaction_style(theme):
    return f"""
QWidget#transactionHeader {{
    min-height: 46px;
    max-height: 46px;
}}


QLabel#transactionHeaderLabel {{
    color: {theme["secondary_text"]};

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1px;
}}
"""