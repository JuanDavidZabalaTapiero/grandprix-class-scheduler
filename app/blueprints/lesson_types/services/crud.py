from app.blueprints.lesson_types.exceptions import (
    LessonTypeAlreadyExists,
    LessonTypeHasLessons,
    LessonTypeNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.lesson_type import LessonType

lesson_type_services = CRUDServices(
    LessonType,
    LessonTypeNotFound,
    unique_fields={"name": LessonTypeAlreadyExists},
    fk_fields={"lessons": LessonTypeHasLessons},
)
