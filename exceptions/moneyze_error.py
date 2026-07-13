class MoneyzeError(Exception):
    def __init(self, title: str, message: str):
        self.title = title
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message