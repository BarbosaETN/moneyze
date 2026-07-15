from exceptions.validation_error import ValidationError
from exceptions.not_found_error import NotFoundError
from exceptions.business_error import BusinessError
from services.base_service import BaseService


class CategoryService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)

    def create(self, **data):


        name = data.get("name", "").strip()

        if len(name) > 50:

            raise ValidationError(
                "O nome da categoria deve possuir no máximo 50 caracteres."
            )

        if self.repository.get_by_name(name):

            raise BusinessError(
                "Já existe uma categoria com esse nome."
            )               

        if not name:
            raise ValidationError(
                "O nome da categoria é obrigatório."
            )

        return super().create(**data)

    def delete_by_id(self, category_id):

        category = self.get_by_id(category_id)

        if category is None:

            raise NotFoundError(
                "Categoria não encontrada."
            )

        return super().delete(category)