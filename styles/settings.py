def get_settings_style(theme):
    return f"""
QFrame#settingsCard {{
    background-color: {theme["card"]};
    border: 1px solid {theme["border"]};
    border-radius: 16px;
}}

QLabel#settingsTitle {{
    color: {theme["text"]};
    font-size: 18px;
    font-weight: 700;
}}

QLabel#settingsDescription {{
    color: {theme["secondary_text"]};
    font-size: 13px;
}}

QFrame#settingsCard QLabel {{
    color: {theme["secondary_text"]};
    font-size: 13px;
    font-weight: 600;
}}

QFrame#settingsCard QLineEdit,
QFrame#settingsCard QComboBox {{
    background-color: {theme["background"]};
    color: {theme["text"]};
    border: 1px solid {theme["border"]};
    border-radius: 10px;
    min-height: 40px;
    padding-left: 12px;
    padding-right: 12px;
}}

QFrame#settingsCard QLineEdit:focus,
QFrame#settingsCard QComboBox:focus {{
    border: 1px solid #16C79A;
}}

QFrame#settingsCard QLineEdit:hover,
QFrame#settingsCard QComboBox:hover {{
    border: 1px solid {theme["secondary_text"]};
}}

QFrame#settingsCard QComboBox::drop-down {{
    border: none;
    width: 32px;
}}

QFrame#settingsCard QComboBox QAbstractItemView {{
    background-color: {theme["card"]};
    color: {theme["text"]};
    border: 1px solid {theme["border"]};
    selection-background-color: {theme["sidebar_active"]};
    selection-color: {theme["sidebar_active_text"]};
    outline: none;
}}

QFrame#settingsCard QLineEdit:disabled,
QFrame#settingsCard QComboBox:disabled {{
    background-color: {theme["card"]};
    color: {theme["secondary_text"]};
}}

QLabel#backupTitle {{
    color: {theme["text"]};
    font-size: 16px;
    font-weight: 700;
}}

QLabel#backupDescription {{
    color: {theme["secondary_text"]};
    font-size: 13px;
}}

QPushButton#backupButton {{
    background-color: #16C79A;
    color: #07111F;
    border: none;
    border-radius: 10px;
    min-height: 40px;
    padding-left: 18px;
    padding-right: 18px;
    font-size: 13px;
    font-weight: 700;
}}

QPushButton#backupButton:hover {{
    background-color: #20D9AA;
}}

QPushButton#backupButton:pressed {{
    background-color: #12A982;
}}

QPushButton#restoreButton {{
    background-color: transparent;
    color: {theme["text"]};
    border: 1px solid {theme["border"]};
    border-radius: 10px;
    min-height: 40px;
    padding-left: 18px;
    padding-right: 18px;
    font-size: 13px;
    font-weight: 600;
}}

QPushButton#restoreButton:hover {{
    background-color: {theme["background"]};
    border-color: {theme["secondary_text"]};
}}
"""