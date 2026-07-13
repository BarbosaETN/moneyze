from sqlalchemy.orm import Session

class BaseRepository:

    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def create(self, **data):
        entity = self.model(**data)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get_all(self):

        return self.session.query(self.model).all()

    def get_by_id(self, entity_id):

        return self.session.get(self.model, entity_id)

    def update(self, entity):
        self.session.commit()
        self.session.refresh(entity)

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()