from views.base.base_page import BasePage


class ExpensePage(BasePage):

    def __init__(self):
        super().__init__(
            "Despesas",
            "Visualize todas as suas despesas."
        )