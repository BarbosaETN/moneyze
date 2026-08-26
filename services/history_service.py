from datetime import date

from repositories.transaction_repository import TransactionRepository


class HistoryService:

    def __init__(
        self,
        repository: TransactionRepository,
    ):
        self.repository = repository

    def get_all(self):

        return self.repository.get_all_ordered()

    def search(self, text: str):

        text = text.strip()

        if not text:
            return self.get_all()

        return self.repository.search(text)

    def get_by_type(self, transaction_type):

        return self.repository.get_by_type(
            transaction_type
        )

    def get_by_date_range(
        self,
        start_date: date,
        end_date: date,
    ):

        return self.repository.get_by_date_range(
            start_date,
            end_date,
        )