from exceptions.moneyze_error import MoneyzeError

class NotFoundError(MoneyzeError):
    def __init__(self, message: str):
        super().__init__(
            "Registro não encontrado",
            message,
        )            