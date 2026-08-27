from exceptions.validation_error import ValidationError
from exceptions.not_found_error import NotFoundError
from exceptions.business_error import BusinessError

from services.base_service import BaseService


class CategoryService(BaseService):

    def __init__(
        self,
        repository,
        transaction_repository=None,
    ):
        super().__init__(repository)

        self.transaction_repository = (
            transaction_repository
        )

    def get_categories_with_summary(
        self,
        start_date,
        end_date,
    ):

        categories = self.repository.get_all()

        categories_summary = []

        for category in categories:

            spent = (
                self.transaction_repository
                .get_expense_total_by_category(
                    category_id=category.id,
                    start_date=start_date,
                    end_date=end_date,
                )
            )

            budget = category.budget

            remaining = budget - spent

            percentage = (
                (spent / budget) * 100
                if budget > 0
                else 0
            )

            categories_summary.append(
                {
                    "id": category.id,
                    "name": category.name,
                    "budget": budget,
                    "spent": spent,
                    "remaining": remaining,
                    "percentage": percentage,
                }
            )

        return categories_summary

    def create(self, **data):

        name = data.get(
            "name",
            "",
        ).strip()

        budget = data.get(
            "budget",
            0,
        )

        if not name:

            raise ValidationError(
                "O nome da categoria é obrigatório."
            )

        if len(name) > 50:

            raise ValidationError(
                "O nome da categoria deve possuir no máximo 50 caracteres."
            )

        if budget < 0:

            raise ValidationError(
                "O orçamento não pode ser negativo."
            )

        if self.repository.get_by_name(name):

            raise BusinessError(
                "Já existe uma categoria com esse nome."
            )

        return super().create(**data)

    def delete_by_id(
        self,
        category_id,
    ):

        category = self.get_by_id(
            category_id
        )

        if category is None:

            raise NotFoundError(
                "Categoria não encontrada."
            )

        return super().delete(
            category
        )