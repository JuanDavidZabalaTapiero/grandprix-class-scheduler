from .services import create_model, delete_model, get_all, get_by_id, update_model


class CRUDServices:
    def __init__(
        self,
        model,
        not_found_exception,
        unique_fields: dict = None,
        fk_fields: dict = None,
    ):
        self.model = model
        self.not_found_exception = not_found_exception
        self.unique_fields = unique_fields or {}
        self.fk_fields = fk_fields or {}

    # === CREATE ===
    def create(self, data: dict):
        return create_model(self.model, data)

    # === READ ===
    def get_by_id(self, entity_id: int):
        return get_by_id(self.model, entity_id, self.not_found_exception)

    def get_all(self):
        return get_all(self.model)

    # === UPDATE ===
    def update(self, instance, data: dict):
        return update_model(instance, data)

    # === DELETE ===
    def delete(self, entity_id: int):
        instance = self.get_by_id(entity_id)
        delete_model(instance)
