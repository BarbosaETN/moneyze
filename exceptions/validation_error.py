from exceptions.moneyze_error import MoneyzeError

class ValidationError(MoneyzeError):
    def __init__(self, message: str):
        super().__init__(
            "Dados inválidos",
            message,
        )            