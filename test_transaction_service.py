from datetime import date

from database.database import initialize_database
from database.connection import get_session
from enums.transaction_type import TransactionType
from repositories.transaction_repository import TransactionRepository
from services.transaction_service import TransactionService


def main():

    initialize_database()

    session = get_session()

    repository = TransactionRepository(session)

    service = TransactionService(repository)

    try:

        transaction = service.create(
            title="",
            description="Salário de agosto",
            amount=4500,
            transaction_type=TransactionType.INCOME,
            transaction_date=date.today(),
            category_id=1,
        )

        print("Transação criada:")
        print(transaction.id)
        print(transaction.title)
        print(transaction.amount)
        print(transaction.transaction_type)

    except Exception as error:

        print("Erro:")
        print(error)

    finally:

        session.close()

    incomes = service.get_incomes()

    print("\nReceitas:")

    for income in incomes:
        print(
            income.id,
            income.title,
            income.amount,
        )


if __name__ == "__main__":
    main()