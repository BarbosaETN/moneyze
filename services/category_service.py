from exceptions.validation_error import ValidationError
from services.base_service import BaseService


class CategoryService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)

    def create(self, **data):

        name = data.get("name", "").strip()

        if not name:
            raise ValidationError(
                "O nome da categoria é obrigatório."
            )

        return super().create(**data)