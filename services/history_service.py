from datetime import date

from repositories.transaction_repository import TransactionRepository


class HistoryService:

    def __init__(self, repository):
        self.repository = repository

    def get_all(self):

        return self.repository.get_all_ordered()

    def get_transactions(
        self,
        transaction_type=None,
        start_date=None,
        end_date=None,
        search_text=None,
    ):

        if search_text:
            search_text = search_text.strip()

        return self.repository.get_filtered(
            transaction_type=transaction_type,
            start_date=start_date,
            end_date=end_date,
            search_text=search_text,
        )

    def search(self, text: str):

        text = text.strip()

        if not text:
            return self.get_all()

        return self.repository.search_by_description(
            text
        )

    def get_by_type(self, transaction_type):

        return self.repository.get_by_type(
            transaction_type
        )

    def get_by_date_range(
        self,
        start_date,
        end_date,
    ):

        return self.repository.get_by_date_range(
            start_date,
            end_date,
        )