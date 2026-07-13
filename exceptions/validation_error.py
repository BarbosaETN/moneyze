from exceptions.moneyze_error import MoneyzeError

class ValidationError(MoneyzeError):
    def __init(self, message: str):
        super().__init__(
            "Dados inválidos",
            message,
        )            