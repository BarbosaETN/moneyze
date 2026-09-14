from exceptions.moneyze_error import MoneyzeError

class BusinessError(MoneyzeError):
    def __init__(self, message: str):
        super().__init__(
            "Operação não permitida",
            message,
        )            