from views.base.base_page import BasePage


class HistoryPage(BasePage):

    def __init__(self):
        super().__init__(
            "Histórico",
            "Visualize todo o seu histórico."
        )