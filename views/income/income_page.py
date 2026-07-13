from views.base.base_page import BasePage


class IncomePage(BasePage):

    def __init__(self):
        super().__init__(
            "Receitas",
            "Visualize todas as suas receitas."
        )