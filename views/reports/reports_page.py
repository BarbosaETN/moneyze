from views.base.base_page import BasePage


class ReportsPage(BasePage):

    def __init__(self):
        super().__init__(
            "Relatórios",
            "Visualize todos os seus relatórios."
        )