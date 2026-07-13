class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, **data):
        return self.repository.create(**data)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, entity_id):
        return self.repository.get_by_id(entity_id)

    def delete(self, entity):
         return self.repository.delete(entity)