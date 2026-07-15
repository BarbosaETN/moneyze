from database.models.category import Category
from repositories.base_repository import BaseRepository

class CategoryRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Category)

    def get_by_name(self, name: str):

        return (
            self.session.query(self.model)
            .filter(self.model.name == name)
            .first()
        )