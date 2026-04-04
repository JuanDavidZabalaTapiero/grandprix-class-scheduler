from app.blueprints.categories.exceptions import CategoryNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.models.category import Category

category_services = CRUDServices(Category, CategoryNotFound)
