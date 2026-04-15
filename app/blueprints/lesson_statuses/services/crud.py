from app.blueprints.lesson_statuses.exceptions import (
    LessonStatusAlreadyExists,
    LessonStatusHasLessons,
    LessonStatusNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.lesson_status import LessonStatus

lesson_status_services = CRUDServices(
    LessonStatus,
    LessonStatusNotFound,
    unique_fields={"name": LessonStatusAlreadyExists},
    fk_fields={"lessons": LessonStatusHasLessons},
)
