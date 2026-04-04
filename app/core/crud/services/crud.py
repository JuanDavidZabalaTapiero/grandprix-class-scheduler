from sqlalchemy.exc import IntegrityError

from app.db.decorators import handle_db_exceptions
from app.db.utils import handle_integrity_error

from .services import create_model, delete_model, get_all, get_by_id, update_model


class CRUDServices:
    def __init__(self, model, not_found_exception, unique_fields: dict = None):
        self.model = model
        self.not_found_exception = not_found_exception
        self.unique_fields = unique_fields or {}

    # === CREATE ===
    @handle_db_exceptions
    def create(self, data: dict):
        try:
            return create_model(self.model, data)

        except IntegrityError as e:
            if self.unique_fields:
                handle_integrity_error(e, self.unique_fields, context=data)
            raise e

    # === READ ===
    def get_by_id(self, entity_id: int):
        return get_by_id(self.model, entity_id, self.not_found_exception)

    def get_all(self):
        return get_all(self.model)

    # === UPDATE ===
    @handle_db_exceptions
    def update(self, instance, data: dict):
        try:
            return update_model(instance, data)

        except IntegrityError as e:
            if self.unique_fields:
                handle_integrity_error(e, self.unique_fields, context=data)
            raise e

    # === DELETE ===
    def delete(self, entity_id: int):
        instance = self.get_by_id(entity_id)
        delete_model(instance)
