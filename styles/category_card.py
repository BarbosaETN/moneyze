from styles.colors import (
    TEXT,
    SECONDARY_TEXT,
    SUCCESS,
    WARNING,
    DANGER,
)


CATEGORY_CARD_STYLE = f"""

#categoryTitle {{

    color: {TEXT};

    font-size: 18px;

    font-weight: bold;

}}


#categoryBudget {{

    color: {SECONDARY_TEXT};

    font-size: 13px;

}}


#categorySectionTitle {{

    color: {SECONDARY_TEXT};

    font-size: 13px;

}}


#categoryExpenseValue {{

    color: {TEXT};

    font-size: 16px;

    font-weight: bold;

}}


#categoryPercentage {{

    font-size: 13px;

    font-weight: bold;

}}


#categoryPercentage[budgetStatus="success"] {{

    color: {SUCCESS};

}}


#categoryPercentage[budgetStatus="warning"] {{

    color: {WARNING};

}}


#categoryPercentage[budgetStatus="danger"] {{

    color: {DANGER};

}}


#categoryRemaining {{

    color: {SECONDARY_TEXT};

    font-size: 13px;

}}


QPushButton#categoryDeleteButton {{

    background-color: transparent;

    border: none;

    border-radius: 8px;

}}


QPushButton#categoryDeleteButton:hover {{

    background-color: rgba(239, 68, 68, 0.15);

}}


QFrame#baseCard[budgetStatus="warning"] {{

    border: 1px solid {WARNING};

}}


QFrame#baseCard[budgetStatus="danger"] {{

    border: 1px solid {DANGER};

}}

QScrollArea#categoryGrid {{

    background-color: transparent;

    border: none;

}}


QWidget#categoryGridContainer {{

    background-color: transparent;

}}

#categoryExceeded {{

    color: {DANGER};

    font-size: 13px;

    font-weight: bold;

}}

"""