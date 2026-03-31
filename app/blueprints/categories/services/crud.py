from app.blueprints.categories.exceptions import CategoryNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.decorators import handle_db_exceptions
from app.db.models.category import Category


class CategoryServices(CRUDServices):

    @handle_db_exceptions
    def create(self, data: dict):
        return super().create(data)

    @handle_db_exceptions
    def update(self, instance, data: dict):
        return super().update(instance, data)


category_services = CategoryServices(Category, CategoryNotFound)
