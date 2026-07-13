from services.base_service import BaseService

class CategoryService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)