def get_sidebar_style(theme):
    return f"""

#appCentralWidget {{

    background-color: {theme["background"]};

}}


#contentStack {{

    background-color: {theme["background"]};

}}


#sidebar {{

    background-color: {theme["sidebar_background"]};

    border-right: 1px solid {theme["sidebar_border"]};

}}


#logoIcon {{

    background-color: #16C79A;

    color: #07111F;

    font-size: 16px;

    font-weight: bold;

    border-radius: 12px;

    min-width: 32px;

    max-width: 32px;

    min-height: 32px;

    max-height: 32px;

}}


#logoTitle {{

    color: {theme["user_name"]};

    font-size: 18px;

    font-weight: bold;

}}


#sidebarDivider {{

    color: {theme["sidebar_border"]};

    background-color: {theme["sidebar_border"]};

    max-height: 1px;

    border: none;

}}


QPushButton#navigationButton {{

    background-color: transparent;

    color: {theme["sidebar_text"]};

    border: none;

    border-radius: 12px;

    text-align: left;

    padding-left: 16px;

    min-height: 42px;

    font-size: 14px;

}}


QPushButton#navigationButton:hover {{

    background-color: {theme["sidebar_hover"]};

    color: {theme["sidebar_text_hover"]};

}}


QPushButton#navigationButton:checked {{

    background-color: {theme["sidebar_active"]};

    color: {theme["sidebar_active_text"]};

    font-weight: bold;

}}


#userCard {{

    background-color: {theme["user_card"]};

    border: 1px solid {theme["user_card_border"]};

    border-radius: 16px;

}}


#userName {{

    color: {theme["user_name"]};

    font-size: 14px;

    font-weight: bold;

}}


#userStatus {{

    color: {theme["user_status"]};

    font-size: 12px;

}}

"""