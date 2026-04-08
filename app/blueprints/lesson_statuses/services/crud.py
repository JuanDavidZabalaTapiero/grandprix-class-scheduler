from app.blueprints.lesson_statuses.exceptions import (
    LessonStatusAlreadyExists,
    LessonStatusNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.lesson_status import LessonStatus

lesson_status_services = CRUDServices(
    LessonStatus,
    LessonStatusNotFound,
    unique_fields={"name": LessonStatusAlreadyExists},
)
