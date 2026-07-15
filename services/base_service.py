from repositories.base_repository import BaseRepository

class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def create(self, **data):
        return self.repository.create(**data)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, entity_id):
        return self.repository.get_by_id(entity_id)

    def delete(self, entity):
         return self.repository.delete(entity)

    def delete_by_id(self, entity_id):

        entity = self.get_by_id(entity_id)

        if entity is None:
            return

        return self.delete(entity)