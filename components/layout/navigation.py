from dataclasses import dataclass
from typing import Type

from PySide6.QtWidgets import QWidget

from views.dashboard.dashboard_page import DashboardPage
from views.categories.category_page import CategoryPage
from views.income.income_page import IncomePage
from views.expenses.expense_page import ExpensePage
from views.history.history_page import HistoryPage
from views.reports.reports_page import ReportsPage
from views.settings.settings_page import SettingsPage


@dataclass(frozen=True)
class NavigationItem:
    id: str
    title: str
    page: Type[QWidget]


NAVIGATION = [
    NavigationItem(
        id="dashboard",
        title="Dashboard",
        page=DashboardPage,
    ),

    NavigationItem(
        id="categories",
        title="Categorias",
        page=CategoryPage,
    ),

    NavigationItem(
        id="income",
        title="Receitas",
        page=IncomePage,
    ),

    NavigationItem(
        id="expense",
        title="Despesas",
        page=ExpensePage,
    ),

    NavigationItem(
        id="history",
        title="Histórico",
        page=HistoryPage,
    ),

    NavigationItem(
        id="reports",
        title="Relatórios",
        page=ReportsPage,
    ),

    NavigationItem(
        id="settings",
        title="Configurações",
        page=SettingsPage,
    ),
]