from app.blueprints.categories.exceptions import (
    CategoryAlreadyExists,
    CategoryHasEnrollments,
    CategoryNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.category import Category

category_services = CRUDServices(
    Category,
    CategoryNotFound,
    unique_fields={"name": CategoryAlreadyExists},
    fk_fields={"enrollments": CategoryHasEnrollments},
)
