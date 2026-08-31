DASHBOARD_SUMMARY_STYLE = """

QWidget#dashboardSummaryCard {
    background-color: #182230;

    border: 1px solid #263548;

    border-radius: 14px;
}


QLabel#dashboardSummaryTitle {
    color: #94A3B8;

    font-size: 13px;

    font-weight: 500;
}


QLabel#dashboardSummaryAmount {
    color: #F8FAFC;

    font-size: 24px;

    font-weight: 700;
}


QLabel#dashboardSummaryVariation {
    font-size: 12px;

    font-weight: 600;
}

"""

CASH_FLOW_SECTION_STYLE = """

QFrame#cashFlowSection {
    background-color: #182230;

    border: 1px solid #263548;

    border-radius: 14px;
}


QLabel#dashboardSectionTitle {
    color: #E5E7EB;

    font-size: 16px;

    font-weight: 600;

    border: none;

    background: transparent;
}


QLabel#dashboardSectionSubtitle {
    color: #94A3B8;

    font-size: 12px;

    border: none;

    background: transparent;
}


QLabel#cashFlowPlaceholder {
    color: #64748B;

    font-size: 13px;

    border: none;

    background: transparent;
}

"""

DASHBOARD_CATEGORY_LIST_STYLE = """

QScrollArea#dashboardCategoryList {
    background-color: transparent;
    border: none;
}


QWidget#dashboardCategoryListContent {
    background-color: transparent;
}


QScrollArea#dashboardCategoryList QScrollBar:vertical {
    background-color: transparent;

    width: 8px;

    margin: 4px 0px 4px 0px;

    border: none;
}


QScrollArea#dashboardCategoryList QScrollBar::handle:vertical {
    background-color: #263548;

    border-radius: 4px;

    min-height: 30px;
}


QScrollArea#dashboardCategoryList QScrollBar::handle:vertical:hover {
    background-color: #334155;
}


QScrollArea#dashboardCategoryList QScrollBar::add-line:vertical,
QScrollArea#dashboardCategoryList QScrollBar::sub-line:vertical {
    height: 0px;

    background-color: transparent;

    border: none;
}


QScrollArea#dashboardCategoryList QScrollBar::add-page:vertical,
QScrollArea#dashboardCategoryList QScrollBar::sub-page:vertical {
    background-color: transparent;
}

"""

DASHBOARD_CATEGORY_CARD_STYLE = """

QFrame#dashboardCategoryCard {
    background-color: #182230;

    border: 1px solid #263548;

    border-radius: 12px;
}


QLabel#dashboardCategoryName {
    color: #E5E7EB;

    font-size: 13px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}


/* =========================
   PORCENTAGEM NORMAL
========================= */

QLabel#dashboardCategoryPercentage {
    color: #94A3B8;

    font-size: 12px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}


/* =========================
   PORCENTAGEM EM ALERTA
========================= */

QLabel#dashboardCategoryPercentageWarning {
    color: #FBBF24;

    font-size: 12px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}


/* =========================
   ORÇAMENTO ULTRAPASSADO
========================= */

QLabel#dashboardCategoryPercentageExceeded {
    color: #F87171;

    font-size: 12px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}


/* =========================
   TEXTO DO ORÇAMENTO
========================= */

QLabel#dashboardCategoryBudget {
    color: #64748B;

    font-size: 11px;

    background-color: transparent;

    border: none;
}


QLabel#dashboardCategoryBudgetExceeded {
    color: #F87171;

    font-size: 11px;

    font-weight: 500;

    background-color: transparent;

    border: none;
}


/* =========================
   BARRA NORMAL
========================= */

QProgressBar#dashboardCategoryProgress {
    background-color: #263548;

    border: none;

    border-radius: 4px;

    height: 8px;
}


QProgressBar#dashboardCategoryProgress::chunk {
    background-color: #34D399;

    border-radius: 4px;
}


/* =========================
   BARRA EM ALERTA
========================= */

QProgressBar#dashboardCategoryProgressWarning {
    background-color: #263548;

    border: none;

    border-radius: 4px;

    height: 8px;
}


QProgressBar#dashboardCategoryProgressWarning::chunk {
    background-color: #FBBF24;

    border-radius: 4px;
}


/* =========================
   BARRA ULTRAPASSADA
========================= */

QProgressBar#dashboardCategoryProgressExceeded {
    background-color: #263548;

    border: none;

    border-radius: 4px;

    height: 8px;
}


QProgressBar#dashboardCategoryProgressExceeded::chunk {
    background-color: #F87171;

    border-radius: 4px;
}

"""

CATEGORY_SECTION_STYLE = """

QFrame#categorySection {
    background-color: transparent;

    border: none;
}


QLabel#categoryEmptyState {
    color: #64748B;

    font-size: 13px;

    background-color: transparent;

    border: none;
}

"""

CASH_FLOW_EMPTY_STATE_STYLE = """

QWidget#cashFlowEmptyState {
    background-color: transparent;

    border: none;
}


QLabel#cashFlowEmptyStateTitle {
    color: #CBD5E1;

    font-size: 14px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}


QLabel#cashFlowEmptyStateDescription {
    color: #64748B;

    font-size: 12px;

    background-color: transparent;

    border: none;
}

"""

CATEGORY_EMPTY_STATE_STYLE = """

QWidget#categoryEmptyState {
    background-color: transparent;

    border: none;
}


QLabel#categoryEmptyStateTitle {
    color: #CBD5E1;

    font-size: 14px;

    font-weight: 600;

    background-color: transparent;

    border: none;
}


QLabel#categoryEmptyStateDescription {
    color: #64748B;

    font-size: 12px;

    background-color: transparent;

    border: none;
}

"""